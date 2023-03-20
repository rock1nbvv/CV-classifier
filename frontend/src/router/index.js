import {createRouter, createWebHistory} from "vue-router";
import CandidateEvaluation from "../components/ResumeEvaluation.vue";
import CandidatesHistory from "@/components/History.vue";

const routes = [
    {
        path: "/",
        name: "CandidateEvaluation",
        component: CandidateEvaluation,
    },
    {
        path: "/history",
        name: "CandidatesHistory",
        component: CandidatesHistory,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
