import { checkDom, setInitFlag } from '../../../js/modules/util/atomic-helpers';
import {
  updateDailyCostAction,
  updateDaysPerWeekAction,
  updateMilesAction,
  updateTransportationAction,
} from './reducers/route-option-reducer';
import inputView from './input-view';
import transitTimeView from './views/transit-time';

const CLASSES = Object.freeze( {
  FORM: 'o-yes-route-option',
  TRANSPORTATION_CHECKBOX: 'a-yes-route-mode',
  QUESTION_INPUT: 'a-yes-question'
} );

const actionMap = Object.freeze( {
  miles: updateMilesAction,
  daysPerWeek: updateDaysPerWeekAction,
  dailyCost: updateDailyCostAction,
} );

/**
 * Map of the fields this form manages that are hidden or shown conditionally,
 * and the predicate functions that determine the field's state
 */
const toggleableFields = {
  'averageCost': ({ transportation }) => transportation && transportation !== 'Drive',
  'miles': (state) => state.transportation === 'Drive',
  'daysPerWeek': (state) => state.transportation === 'Drive' || state.isCostPerDay
};

function hideToggleableField(node) {
  node.value = '';
  node.classList.add('u-hidden');
}

function showToggleableField(node) {
  node.classList.remove('u-hidden');
}

function updateVisibleInputs(inputs, { route: prevState }, { route: state }) {
  console.log(arguments)
  for (let name in toggleableFields) {
    const predicate = toggleableFields[name]; 
    const lastValue = prevState[name];
    const currentValue = state[name];
    const stateHasChanged = lastValue !== currentValue || (!lastValue && !currentValue);

    if (stateHasChanged) {
      const node = inputs[name];
      predicate(state) ? showToggleableField(node) : hideToggleableField(node)
    }
  } 
}

/**
 * RouteOptionFormView
 * @class
 *
 * @classdesc Initializes the organism.
 *
 * @param {HTMLNode} element
 *  The root DOM element for this view
 * @returns {Object} The view's public methods
 */
function RouteOptionFormView( element, { store, routeIndex } ) {
  const _dom = checkDom( element, CLASSES.FORM );
  const _transportationOptionEls = Array.prototype.slice.call(
    _dom.querySelectorAll( `.${ CLASSES.TRANSPORTATION_CHECKBOX }` )
  );
  const _textInputEls = Array.prototype.slice.call(
    _dom.querySelectorAll( `.${ CLASSES.QUESTION_INPUT }` )
  );
  const _inputMap = _textInputs.reduce((memo, node) => {
    memo[node.querySelector('input').getAttribute('data-js-name')] = node;

    return memo;
  }, {});

  /**
   * Updates form state from child input text nodes
   * @param {object} updateObject object with DOM event and field name
   */
  function _setQuestionResponse( { name, event } ) {
    const action = actionMap[name];
    const { target: { value } } = event;

    if ( action ) {
      store.dispatch( action( {
        routeIndex,
        value
      } ) );
    }
  }

  /**
   * Updates state from child input radio nodes
   * @param {object} updateObject object with DOM event and field name
   */
  function _setSelected( { event } ) {
    const { target: { value } } = event;

    store.dispatch( updateTransportationAction( {
      routeIndex,
      value } ) );
  }

  /**
   * Initialize checkbox nodes this form view manages
   */
  function _initRouteOptions() {
    _transportationOptionEls.forEach( node => inputView( node, {
      events: { click: _setSelected },
      type: 'radio'
    } )
      .init()
    );
  }

  /**
   * Initialize input nodes this form view manages
   */
  function _initQuestions() {
    _textInputEls.forEach( node => inputView( node, {
      events: { input: _setQuestionResponse }
    } )
      .init()
    );
  }

  return {
    init() {
      if ( setInitFlag( _dom ) ) {
        _initRouteOptions();
        _initQuestions();
        transitTimeView(_dom.querySelector('.m-yes-transit-time'), { store }).init();

        const boundUpdate = updateVisibleInputs.bind(null, _inputMap);
        const currentState = store.getState();

        boundUpdate(currentState, currentState);
        
        store.subscribe(boundUpdate);
      }
    }
  };
}

RouteOptionFormView.CLASSES = CLASSES;

export default RouteOptionFormView;
