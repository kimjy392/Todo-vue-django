<template>
  <div class="todo-list">
      <h2>아기상어</h2>
      <ul>
        <li v-for="todo in todos" :key="todo.id">
          <input @change="updateTodo(todo)" v-model="todo.is_completed" type="checkbox">
        {{ todo.title }}
        <button @click="deleteTodo(todo)">X</button>
        </li> 
      </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name :"TodoList",
    props: {
        todos : {
            type: Array,
            required: true
        }
    },
    methods: {
      deleteTodo(todo) {
        console.log(todo)
        this.$session.start()
        const token = this.$session.get('jwt')
        const options = {
        headers: {
          Authorization : `JWT ${token}` // JWT 다음에 공백있음!
        }
      }
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, options)
          .then(response => {
            console.log(response)
            const target = this.todos.find(el => {
              return el === todo
            })
            const idx = this.todos.indexOf(target)
            if (idx > -1) {
              this.todos.splice(idx, 1)
            }
          })
          .catch(error => {
            console.log(error)
          })
      },
      updateTodo(todo) {
        this.$session.start()
        const token = this.$session.get('jwt')
        const options = {
        headers: {
          Authorization : `JWT ${token}` // JWT 다음에 공백있음!
          }
        }
        axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, todo, options)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
}
</script>

<style>

</style>