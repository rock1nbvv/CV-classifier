<template>
  <div v-for="(candidate, index) in candidateHistory" :key="index">
    <div
      class="card"
      style="
        width: 18rem;
        float: left;
        position: relative;
        margin-left: 20px;
        margin-bottom: 10px;
      "
    >
      <div class="card-body">
        <h5 class="card-title">{{ candidate.brand }} {{ candidate.name }}</h5>
        <p class="card-text">Age: {{ candidate.age }}</p>
        <p>Mileage: {{ candidate.mileage }}</p>
        <p>Repairments: {{ candidate.repairments }}</p>
        <p>Evaluated Price: {{ candidate.est_price }}</p>
        <!--        <a href="#" class="btn btn-primary">Go somewhere</a>-->
      </div>
    </div>
    <p></p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      candidateHistory: [],
    };
  },
  async created() {
    await this.getHistory();

    this.candidateHistory = Array.from(this.candidates);
  },
  methods: {
    async sendRequest(url, method, data) {
      const myHeaders = new Headers({
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
      });

      const response = await fetch(url, {
        method: method,
        headers: myHeaders,
        body: data,
      });

      return response;
    },
    async getHistory() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getAllRanks",
        "get"
      );
      this.candidates = await response.json();
    },
  },
};
</script>
