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
                    for (var value in variables){
                        console.log(value)
                    }
                    url = this.backend + "/getEmails";
                    url = ""
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
