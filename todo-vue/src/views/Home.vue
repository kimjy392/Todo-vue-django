<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <TodoList/>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoList from '@/components/TodoList.vue'
import axios from 'axios'
export default {
  name: 'home',
  components: {
    TodoList
  },
  data() {
    return {
      todos: [],
    }
  },
  mounted() {
    // axios 요청
    axios.get('http://127.0.0.1:8000/api/v1/todos')
      .then(response => {
        console.log(response) // 만약, 오류가 발생하면 
      })
  }
}
</script>
