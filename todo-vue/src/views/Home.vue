<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- 이벤트 리스너 등록 -->
    <TodoForm @todoCreate-event="TodoCreate"/> <!-- pascalcase, uppercamelcase -->
    <!-- kebab-case -->
    <TodoList  :todos="todos"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'
import axios from 'axios'
export default {
  name: 'home',
  components: {
    TodoList,
    TodoForm
  },
  data() {
    return {
      todos: [],
    }
  },
  methods: {
    TodoCreate(title) {
      console.log('==부모컴포넌트==')
      console.log(title)
      const data = {
        title: title,
        user: 1
      }
      // request.POST인 경우는 FormData!!
      // const formData = new FormData()
      // formData.append('title', title)
      // formData.append('user', 1)
      axios.post('http://127.0.0.1:8000/api/v1/todos/', data)
        .then(response => {
          console.log(response)
          this.todos.push(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    getTodos() {
      // axios 요청
      axios.get('http://127.0.0.1:8000/api/v1/todos/')
        .then(response => {
          console.log(response) // 만약, 오류가 발생하게 되면 ESLint 설정을 package.json에 추가
          this.todos = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
  mounted() {
    this.getTodos()
  }
}
</script>
