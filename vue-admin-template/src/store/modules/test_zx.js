import { test_zx_1, logout } from '@/api/testzx'

import { resetRouter } from '@/router'

const state = {
  name: '',
  req_test: null,
};

const mutations = {
  SET_RES(state, data) {
    state.req_test = data;
    console.log(state.req_test);
  }
}

const actions = {
  
  test_zx_m({commit}, project) {
    
    return new Promise((resolve, reject) => {
      test_zx_1(project).then(response => {
        commit('SET_RES', response);
      }).catch(error => {
        reject(error)
      })
    })
  }

}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

