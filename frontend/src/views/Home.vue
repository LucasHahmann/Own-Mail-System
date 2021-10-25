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
        </v-app>
    </div>
</template>

<script>
import api from "@/methods/api.js"
import store from "@/store/index.js"
import AppBar from "@/components/Navigation/AppBar.vue"
export default {
    components:{
        AppBar
    },
    data () {
        return {
            mails: []
        }
    },
    created () {
        this.getMails()
    },
    mixins: [api],
    methods: {
        async getMails(){
            this.mails = await this.fatch("getMails", [store.state.username, store.state.password])
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