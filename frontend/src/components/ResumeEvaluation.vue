<template>
  <div class="container">
    <div class="row">
      <div class="col-6 mx-auto mt-5">
        <h1>CV classifier</h1>
        <p>Please fill the form</p>
        <form @submit.prevent="evaluateCandidate" class="mx-auto">
          <div class="row">
            <div class="col-9">
              <div class="mb-3">
                <label for="nameInput" class="form-label"
                  >Your name: {{ name }}</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="nameInput"
                  v-model="name"
                  placeholder="Your name"
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Quality management</label>
                <select
                  class="form-select"
                  id="brand"
                  v-model="form.quality_management"
                >
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Scope management</label>
                <select
                  class="form-select"
                  id="brand"
                  v-model="form.scope_management"
                >
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Risk management</label>
                <select
                  class="form-select"
                  id="brand"
                  v-model="form.risk_management"
                >
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Test documentation</label>
                <select
                  class="form-select"
                  id="brand"
                  v-model="form.documentation"
                >
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Automation testing</label>
                <select
                  class="form-select"
                  id="brand"
                  v-model="form.automation"
                >
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">English language</label>
                <select class="form-select" id="brand" v-model="form.english">
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Knowledge of STLC</label>
                <select class="form-select" id="brand" v-model="form.stlc">
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Knowledge of SDLC</label>
                <select class="form-select" id="brand" v-model="form.sdlc">
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Knowledge of git</label>
                <select class="form-select" id="brand" v-model="form.git">
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Knowledge of Docker</label>
                <select class="form-select" id="brand" v-model="form.docker">
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Unit testing</label>
                <select
                  class="form-select"
                  id="brand"
                  v-model="form.unit_testing"
                >
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Knowledge of Java</label>
                <select class="form-select" id="brand" v-model="form.java">
                  <option
                    v-for="(value, index) in options"
                    v-bind:value="value"
                    v-bind:key="index"
                  >
                    {{ value }}
                  </option>
                </select>
              </div>
              <div class="mb-3" v-if="predictedRank !== null">
                <p>
                  Your predicted rating: {{ predictedRank }}, your rank
                  {{ est_class }}
                </p>
              </div>
            </div>
            <div class="mb-3">
              <button class="btn btn-success" type="submit">Check Value</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      predictedRank: null,
      est_class: "",
      name: "",
      form: {
        quality_management: "",
        scope_management: "",
        risk_management: "",
        documentation: "",
        automation: "",
        english: "",
        stlc: "",
        sdlc: "",
        git: "",
        docker: "",
        unit_testing: "",
        java: "",
      },
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
    async evaluateCandidate() {
      console.log(this.form.quality_management);
      const candidate = {
        name: this.name,
        form: this.form,
      };
      console.log(JSON.stringify(candidate));
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/evaluate",
        "post",
        JSON.stringify(candidate)
      );
      const temp = await response.json();
      this.predictedRank = temp.rank;
      this.predictedRank = temp.estimated_class;
    },
  },
};
</script>
