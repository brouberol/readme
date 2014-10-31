angular.module('app', []);

function RecoCtrl (RecoService) {
  this.items = RecoService.getRecommendations();
  console.log(this.items);
};


// implement it with ressource?
function RecoService ($http) {
  this.getRecommendations = function () {
    $http.get('/api/recommendation').
    success(function (data, status, headers, config) {
      return data['objects'];
    }).
    error(function (data, status, headers, config) {
      return data['objects'] || "Request failed";
    });
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

