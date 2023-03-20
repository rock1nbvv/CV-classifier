<template>
  <div class="container">
    <div class="row">
      <div class="col-6 mx-auto mt-5">
        <div class="mb-3">
          <li v-for="(candidate, index) in candidateHistory" :key="index">
            <h5>
              {{ candidate.name }}: {{ candidate.estimated_class }} -
              {{ candidate.rank }}
            </h5>
            <div class="mb-3" v-if="!candidate.hr_interviewed">
              HR grade
              <select class="form-select" v-model="hr_grade">
                <option
                  v-for="(value, index) in options"
                  v-bind:value="value"
                  v-bind:key="index"
                >
                  {{ value }}
                </option>
              </select>
              <button
                @click="submitInterview(candidate.id, 'hr')"
                class="btn btn-success"
              >
                Submit HR interview
              </button>
            </div>
            <div class="mb-3" v-if="!candidate.tech_interviewed">
              Tech grade
              <select class="form-select" v-model="tech_grade">
                <option
                  v-for="(value, index) in options"
                  v-bind:value="value"
                  v-bind:key="index"
                >
                  {{ value }}
                </option>
              </select>
              <button
                @click="submitInterview(candidate.id, 'tech')"
                class="btn btn-success"
              >
                Submit Tech interview
              </button>
            </div>
          </li>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      interview: "",
      selected: "",
      candidateHistory: [],
      hr_grade: "",
      tech_grade: "",
      options: [
        "None to very little",
        "Extremely low",
        "Very low",
        "Low",
        "More or less low",
        "Somewhat low",
        "Moderately low",
        "From low to more or less fair",
        "From fair to more or less high",
        "More or less high",
        "Somewhat high",
        "Moderately high",
        "High",
        "Very high",
        "Extremely high",
      ],
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
    async printConsole(id, type) {
      console.log(id);
      console.log(type);
    },
    async submitInterview(id, type) {
      let grade = "";
      if (type === "hr") {
        grade = this.hr_grade;
      } else {
        grade = this.tech_grade;
      }
      const candidate = {
        type: type,
        grade: grade,
      };
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/interview/" + id,
        "post",
        JSON.stringify(candidate)
      );

      return response.json();
    },
  },
};
</script>
