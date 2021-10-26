<template>
    <div>
        <v-app-bar>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
            <v-spacer></v-spacer>
            <v-text-field v-model="search" label="Search" outlined append-icon="mdi-magnify"></v-text-field>
            <!-- Profil Menu -->
            <div class="text-center">
                <v-menu v-model="menu" :close-on-content-click="false" :nudge-width="200" offset-x>
                    <template v-slot:activator="{ on, attrs }">
                        <v-avatar color="indigo" v-bind="attrs" v-on="on">
                            <v-icon dark @click="show = !show">
                                mdi-account-circle
                            </v-icon>
                        </v-avatar>
                    </template>

                    <v-card>
                        <v-list>
                            <v-list-item>
                                <v-list-item-avatar>
                                    <v-avatar color="indigo">
                                        <v-icon dark>
                                            mdi-account-circle
                                        </v-icon>
                                    </v-avatar>
                                </v-list-item-avatar>

                                <v-list-item-content>
                                    <v-list-item-title>{{ firstname }} {{ lastname }} </v-list-item-title>
                                    <!-- <v-list-item-subtitle>Founder of Vuetify</v-list-item-subtitle> -->
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>

                        <v-divider></v-divider>
                        <v-list>
                            <div v-for="(account, counter) in accounts[0].Accounts" :key="counter">
                                <v-list-item>
                                    {{account.username}}
                                </v-list-item>
                            </div>
                        </v-list>
                        <v-list>
                            <v-list-item>
                                <v-list-item-action>
                                    <v-btn @click="showLogin = !showLogin" v-show="showLogin">Add account</v-btn>
                                    <div v-show="!showLogin">
                                        <v-text-field v-model="username" label="Username" append-icon="mdi-account"></v-text-field>
                                        <v-text-field v-model="password" label="Password" append-icon="mdi-lock"></v-text-field>
                                        <v-btn @click="addAccount()">Submit</v-btn>
                                    </div>
                                </v-list-item-action>
                            </v-list-item>
                        </v-list>
                    </v-card>
                </v-menu>
            </div>
            <!-- End Profil Menu -->
        </v-app-bar>

        
        <div>
            <v-snackbar
                v-model="snackbar"
                :timeout="timeout"
                :color="snackbarColor"
                >
                {{ snackbarText }}
            </v-snackbar>
        </div>

    </div>
</template>

<script>
//import store from "@/store/index.js"
import api from "@/methods/api.js"
export default {
    mixins: [api],
    created () {
        if (this.$cookies.get("Accounts") == null) this.addCookies()
        this.accounts = [{"Accounts":[{
            "username": "dsdsd",
            "password": "dsihdf"
        },
        {
            "username": "dsds",
            "password": "dsidsdhdf"
        }
        ]}]
        console.log(this.accounts)

    },
    methods: {
        async addCookies(){
            this.$cookies.set("Accounts", [{"username":"sdd"}], "5h")
        },
        async addAccount(){
            //var res = await this.fatch("checkLogin", [this.username, this.password])
            var res = true;
            if(res){
                this.snackbarColor = "green"
                this.snackbarText = "Successfully added Account"
                this.snackbar = true;
                var acc = JSON.stringify(this.$cookies.get("Accounts"))
                acc =JSON.parse(acc)
                console.log(acc)
                acc.push({"username":this.username, "password":this.password})
                try{
                    acc.push({"username":this.username, "password":this.password})
                } catch{
                    acc = {"username":this.username, "password":this.password}
                }
                
                this.$cookies.remove("Account")

                this.$cookies.set("Accounts", acc, "5h")
                console.log(this.$cookies.get("Accounts"))
                this.username, this.password = ""
                this.showLogin = !this.showLogin
            } else{
                this.snackbarColor = "red"
                this.snackbarText = "Login data not correct."
                this.snackbar = true;
                this.username, this.password = ""
            }
        }
    },
    components:{
        
    },
    data () {
    return {
        accounts: [],
        menu: false,
        showLogin: true,
        search: "",
        show: false,
        firstname: "",
        lastname: "",
        username: "",
        password: "",
        snackbar: false,
        timeout: 3000,
        snackbarText: "",
        snackbarColor: ""
    }
  },
    
}
</script>

<style>
.v-toolbar .v-input {
margin-top: 25px;
}

</style>