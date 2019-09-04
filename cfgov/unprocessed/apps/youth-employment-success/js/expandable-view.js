import { checkDom, setInitFlag } from '../../../js/modules/util/atomic-helpers';

const CLASSES = Object.freeze({
  CONTAINER: 'o-expandable'
});

function expandableView(element, { expandable }) {
  const _dom = checkDom(element, CLASSES.CONTAINER);

  if (!expandable) {
    throw new Error('An instance of an expandable is a required prop.');
  }

  function _hideRouteDetails() {

  }

  function _showRouteDetails() {

  }

  return {
    init() {
      if (!setInitFlag(_dom)) {
        expandable.transition.addEventListener('expandBegin', _hideRouteDetails);
        expandable.transition.addEventListener('collapseEnd', _showRouteDetails);
      }
    }
  }
}

export default expandableView;
