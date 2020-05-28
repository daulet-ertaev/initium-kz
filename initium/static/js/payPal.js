var app = new Vue({
  el: '#app',
  data(){
    return {
        renderComponent: true,
    };
  },
  methods: {
    forceRerender() {
        // Remove my-component from the DOM
        this.renderComponent = false;

        this.$nextTick(() => {
          // Add the component back in
          this.renderComponent = true;
        });
      }
  }
})