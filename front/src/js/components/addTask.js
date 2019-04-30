angular
  .module('tasklistApp')
  .component('addTask', {
    templateUrl: 'views/addTask.html',

    controller: function addTaskController($http, $scope) {
      this.clearAddForm = function() {
        $scope.task = null;
      }

      this.addItem = function(task) {
        $http.post(
          apiUrl + '/tasks',
          JSON.stringify({name: task.name, task_list_id: this.taskListId})
        ).then(function successCallback(response) {
          $scope.$parent.taskList.tasks.push(response.data);
          this.clearAddForm();
        }.bind(this));
      };

    },
    bindings: {
        taskListId: '<', // or key: '<' it depends on what binding you need
    }
  });
