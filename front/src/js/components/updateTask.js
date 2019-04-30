angular
  .module('tasklistApp')
  .component('updateTask', {
    templateUrl: 'views/updateTask.html',

    controller: function updateTaskController($http, $scope) {
      this.updateTask = function(task) {
        $http.patch(
          apiUrl + '/tasks/' + task.id,
          JSON.stringify({name: task.name})
        ).then(function successCallback(response) {
          const element = $scope.$parent.taskList.tasks.find(x => x.id === task.id);
          element.name = response.data.name;
        }.bind(this));
      };
    },
    bindings: {
        task: '<' // or key: '<' it depends on what binding you need
    }
  });
