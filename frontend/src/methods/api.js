export default {
    data: () => ({
        check: false,
        tokenCheck: true,
        backend: "http://localhost:5000/api"
    }),
    methods: {
        async fatch(endpoint, variables){
            var _this = this;
            var url = "";
            var fetchMethod = "";
            var b0dy= null;
            switch(endpoint) {
                case "getMails":
                    console.log(variables)
                    url = this.backend + `/getEmails/${variables[0]}/${variables[1]}`
                    fetchMethod = "POST";
                    console.log(url)
                    // url = "http://localhost:5000/api/getEmails/n300538_0-cdo/2aIl%UYApYy94&h"
                    break
                case "checkLogin":
                    url = this.backend + `/checkLogin/${variables[0]}/${variables[1]}`;
                    fetchMethod = "POST";
                }
                
                
                // Set the fetch with variables
                var resfetch = await fetch(url, {method: fetchMethod,
                    headers: {
                        'Content-Type': 'application/json',},body: b0dy})
                    .then(async function(response){
                        if(response.status != 200){
                            _this.check= true;
                        }
                        return response.json();})
                    .then(async function (data) {
                        if(_this.check == true){
                            console.log("Fehler");
                        }
                        return data;})
                    return resfetch;
        },
    }
}
