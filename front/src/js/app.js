const app = angular.module('tasklistApp', [
  'ngRoute'
])

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
    .when('/', {
      templateUrl: 'views/welcome.html'
    })
    .when('/tasklist/:taskListId', {
      template: '<task-list></task-list>'
    })
    .otherwise({
      redirectTo: '/'
    });
  }
]);
