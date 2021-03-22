<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="项目id：">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  
  <el-form-item>
    <el-button type="primary" @click="onSubmit">证实</el-button>
  </el-form-item>
  
  <div v-if="req_test">
     <input v-model="req_test.name">
     <input v-model="req_test.age" type="text">
      <el-input type="text" v-model="req_test.age" ></el-input>

   </div>


</el-form>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  data() {
    return {
      form: {
        name: '',
      }

    }
  },

  computed: {
    ...mapState('test_zx', [
      'req_test',
    ])
  },


  methods: {
    onSubmit() {

        this.$store.dispatch('test_zx/test_zx_m', this.form).then(() => {
            this.$router.push({ path: this.redirect || '/' })
            this.loading = false
          }).catch(() => {
            this.loading = false
          })

    }

  }
}
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

