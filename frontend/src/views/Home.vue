<template>
    <div>
        <v-app>
            <div class="navbar">
                <AppBar/>
            </div>
            <v-container v-for="(mail, counter) in mails[0].mails" :key="mail.Id" class="mailContainer">
                <v-row @click="selectMail(counter)">
                    <v-col classs="itemContainer">
                        <p>{{ mail.ID}}</p>
                    </v-col>
                    <v-col>
                        <p>From: {{ mail.From}}</p>
                    </v-col>
                    <v-col>
                        <p>Subject: {{ mail.Subject }}</p>
                    </v-col>
                </v-row>
            </v-container>
            <!-- Login prompt -->
                <div class="text-center">
                    <v-dialog v-model="loginForm" width="500">
                        <v-card>
                            <v-card-title class="text-h5 grey lighten-2">
                                Login
                            </v-card-title>

                            <v-card-text>
                                <v-text-field v-model="username" label="Username" append-icon="mdi-account"></v-text-field>
                                <v-text-field v-model="password" label="Password" append-icon="mdi-lock"></v-text-field>
                            </v-card-text>

                            <v-divider></v-divider>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" text @click="addCookies()">
                                    Login
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </div>
            <!-- End Login prompt -->
        </v-app>
    </div>
</template>

<script>
import api from "@/methods/api.js"
// import store from "@/store/index.js"
import AppBar from "@/components/Navigation/AppBar.vue"
export default {
    components:{
        AppBar
    },
    data () {
        return {
            mails: [{"mails":[]}],
            loginForm: false,
            username: "",
            password: ""
        }
    },
    async created () { 
        if(await this.checkLogin()) this.getMails();
    },
    mixins: [api],
    methods: {
        async checkLogin(){
            if(this.$cookies.get("Username") != null) return true
            this.loginForm = true;
        },
        async addCookies(){
            this.$cookies.set("Username", this.username, "5h")
            this.$cookies.set("Password", this.password, "5h")
            this.getMails()
            this.loginForm = false;
        },
        async getMails(){
            this.mails = await this.fatch("getMails", [this.$cookies.get("Username"), this.$cookies.get("Password")])
        },
        selectMail(counter){
            console.log(this.mails[0].mails[counter])
        }
    },
    
}
</script>

<style>
.mailContainer{
    border-style: solid;
    border-width: 3px;
    border-radius: 5;
}
.itemContainer{
    border-right: 6px;
}
</style>