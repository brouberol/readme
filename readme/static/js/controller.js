angular.module('app', []);

function RecoCtrl (RecoService) {
  var ctrl = this;
  RecoService.getRecommendations().success(
    function (data, status, headers, config) {
      ctrl.items = data.objects;
    }
  );
};


function RecoService ($http) {
  return {
    getRecommendations: function () {
      return $http.get('/api/recommendation');
    },
  };
}


// Definition of all services
angular
  .module('app')
  .service('RecoService', RecoService);

// Definition of all controllers
angular
  .module('app')
  .controller('RecoCtrl', ['RecoService', RecoCtrl]);

