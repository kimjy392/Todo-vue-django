<template>
  <form class="todo-form" @submit.prevent="todoCreate">
      <label for="title">todo: </label>
      <input v-model="title" type="text" id="title">
      <button type="submit">등록</button>
  </form>
</template>

<script>
export default {
    name:'TodoForm',
    data() {
        return {
            title: ''
        }
    },
    methods: {
        todoCreate() {
            // form이 제출 되는 경우 해당 함수 실행
            // 부모 컴포넌트로 이번테 발생($emit)을 통해 데이터 전달
            this.$emit('todoCreate-event', this.title)
            this.title = ''
        }
    }

}
</script>

<style>

</style>