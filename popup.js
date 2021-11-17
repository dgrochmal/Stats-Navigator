document.addEventListener('DOMContentLoaded', function () {

    var fanButton = document.getElementById('bbRef');
    fanButton.addEventListener('click', function () {
        var query = { active: true, currentWindow: true };
        function callback(tabs) {
            var currentTab = tabs[0]; // there will be only one in this array
            console.log(currentTab.url); // also has properties like currentTab.id
            var currentLocation = currentTab.url;
            if (currentLocation.substring(12, 21) === "fangraphs") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 8)
                console.log(playersStringTillEnd)
                var indexOfQuestionMark = playersStringTillEnd.indexOf("/");
                console.log(indexOfQuestionMark);
                var nameAndId = playersStringTillEnd.substring(indexOfQuestionMark + 1);
                console.log(nameAndId);
                var indexOfSecondSlash = nameAndId.indexOf("/");
                console.log(indexOfSecondSlash);
                var id = nameAndId.substring(0, indexOfSecondSlash);
                console.log(id);

                fetch("../data/fangraphs.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.update({
                                url: "https://www.baseball-reference.com"
                            });
                        } else {
                            var lastName = player.name_last;
                            var initial = lastName[0];

                            chrome.tabs.update({
                                url: `https://www.baseball-reference.com/players/${initial}/${player.key_bbref}.shtml`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(12, 30) === "baseball-reference") {
                //They clicked the bb reference button, so they're already here?
            }
            else if (currentLocation.substring(8, 22) === "baseballsavant") {
                var locationOfPlayersString = currentLocation.indexOf('savant-player');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 14)
                console.log(playersStringTillEnd)
                var indexOfQuestionMark = playersStringTillEnd.indexOf("?");
                console.log(indexOfQuestionMark);
                var nameAndId = playersStringTillEnd.substring(0, indexOfQuestionMark);
                console.log(nameAndId);
                var id = nameAndId.substring(nameAndId.search(/\d/));
                console.log(id);

                fetch("../data/mlbam.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.update({
                                url: "https://www.baseball-reference.com"
                            });
                        } else {

                            var lastName = player.name_last;
                            var initial = lastName[0];

                            chrome.tabs.update({
                                url: `https://www.baseball-reference.com/players/${initial}/${player.key_bbref}.shtml`
                            });
                        }
                    }
                    );
            }
            else {
                chrome.tabs.update({
                    url: "https://www.baseball-reference.com"
                });
            }
        }
        chrome.tabs.query(query, callback);
    }, false);
    fanButton.addEventListener('contextmenu', function (ev) {
        ev.preventDefault();
        var query = { active: true, currentWindow: true };
        function callback(tabs) {
            var currentTab = tabs[0]; // there will be only one in this array
            console.log(currentTab.url); // also has properties like currentTab.id
            var currentLocation = currentTab.url;
            if (currentLocation.substring(12, 21) === "fangraphs") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 8)
                console.log(playersStringTillEnd)
                var indexOfQuestionMark = playersStringTillEnd.indexOf("/");
                console.log(indexOfQuestionMark);
                var nameAndId = playersStringTillEnd.substring(indexOfQuestionMark + 1);
                console.log(nameAndId);
                var indexOfSecondSlash = nameAndId.indexOf("/");
                console.log(indexOfSecondSlash);
                var id = nameAndId.substring(0, indexOfSecondSlash);
                console.log(id);

                fetch("../data/fangraphs.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.create({
                                url: "https://www.baseball-reference.com"
                            });
                        } else {

                            var lastName = player.name_last;
                            var initial = lastName[0];

                            chrome.tabs.create({
                                url: `https://www.baseball-reference.com/players/${initial}/${player.key_bbref}.shtml`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(12, 30) === "baseball-reference") {
                //They clicked the bb reference button, so they're already here?
            }
            else if (currentLocation.substring(8, 22) === "baseballsavant") {
                var locationOfPlayersString = currentLocation.indexOf('savant-player');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 14)
                console.log(playersStringTillEnd)
                var indexOfQuestionMark = playersStringTillEnd.indexOf("?");
                console.log(indexOfQuestionMark);
                var nameAndId = playersStringTillEnd.substring(0, indexOfQuestionMark);
                console.log(nameAndId);
                var id = nameAndId.substring(nameAndId.search(/\d/));
                console.log(id);

                fetch("../data/mlbam.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.create({
                                url: "https://www.baseball-reference.com"
                            });
                        } else {

                            var lastName = player.name_last;
                            var initial = lastName[0];

                            chrome.tabs.create({
                                url: `https://www.baseball-reference.com/players/${initial}/${player.key_bbref}.shtml`
                            });
                        }
                    }
                    );
            }
            else {
                chrome.tabs.create({
                    url: "https://www.baseball-reference.com"
                });
            }
        }
        chrome.tabs.query(query, callback);
        return false;
    }, false);


    var fanButton = document.getElementById('savant');
    fanButton.addEventListener('click', function () {

        var query = { active: true, currentWindow: true };
        function callback(tabs) {
            var currentTab = tabs[0]; // there will be only one in this array
            console.log(currentTab.url); // also has properties like currentTab.id
            var currentLocation = currentTab.url;
            if (currentLocation.substring(12, 21) === "fangraphs") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 8)
                console.log(playersStringTillEnd)
                var id = playersStringTillEnd.indexOf("/");
                console.log(id);
                var nameAndId = playersStringTillEnd.substring(id + 1);
                console.log(nameAndId);
                var indexOfSecondSlash = nameAndId.indexOf("/");
                console.log(indexOfSecondSlash);
                var id = nameAndId.substring(0, indexOfSecondSlash);
                console.log(id);

                fetch("../data/fangraphs.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.update({
                                url: "https://baseballsavant.mlb.com"
                            });
                        } else {

                            chrome.tabs.update({
                                url: `https://baseballsavant.mlb.com/savant-player/${player.name_first}-${player.name_last}-${player.key_mlbam}`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(12, 30) === "baseball-reference") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 10)
                console.log(playersStringTillEnd)
                var id = playersStringTillEnd.substring(0, playersStringTillEnd.length - 6);
                console.log(id);;

                fetch("../data/bbref.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.update({
                                url: "https://baseballsavant.mlb.com"
                            });
                        } else {

                            chrome.tabs.update({
                                url: `https://baseballsavant.mlb.com/savant-player/${player.name_first}-${player.name_last}-${player.key_mlbam}`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(8, 22) === "baseballsavant") {
                //They clicked the savant button, so they're already here?
            }
            else {
                chrome.tabs.update({
                    url: "https://baseballsavant.mlb.com"
                });
            }
        }
        chrome.tabs.query(query, callback);
    }, false);
    fanButton.addEventListener('contextmenu', function (ev) {
        ev.preventDefault();
        var query = { active: true, currentWindow: true };
        function callback(tabs) {
            var currentTab = tabs[0]; // there will be only one in this array
            console.log(currentTab.url); // also has properties like currentTab.id
            var currentLocation = currentTab.url;
            if (currentLocation.substring(12, 21) === "fangraphs") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 8)
                console.log(playersStringTillEnd)
                var id = playersStringTillEnd.indexOf("/");
                console.log(id);
                var nameAndId = playersStringTillEnd.substring(id + 1);
                console.log(nameAndId);
                var indexOfSecondSlash = nameAndId.indexOf("/");
                console.log(indexOfSecondSlash);
                var id = nameAndId.substring(0, indexOfSecondSlash);
                console.log(id);

                fetch("../data/fangraphs.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.create({
                                url: "https://baseballsavant.mlb.com"
                            });
                        } else {

                            chrome.tabs.create({
                                url: `https://baseballsavant.mlb.com/savant-player/${player.name_first}-${player.name_last}-${player.key_mlbam}`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(12, 30) === "baseball-reference") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 10)
                console.log(playersStringTillEnd)
                var id = playersStringTillEnd.substring(0, playersStringTillEnd.length - 6);
                console.log(id);;

                fetch("../data/bbref.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.create({
                                url: "https://baseballsavant.mlb.com"
                            });
                        } else {

                            chrome.tabs.create({
                                url: `https://baseballsavant.mlb.com/savant-player/${player.name_first}-${player.name_last}-${player.key_mlbam}`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(8, 22) === "baseballsavant") {
                //They clicked the savant button, so they're already here?
            }
            else {
                chrome.tabs.create({
                    url: "https://baseballsavant.mlb.com"
                });
            }
        }
        chrome.tabs.query(query, callback);
        return false
    }, false);

    var fanButton = document.getElementById('fan');
    fanButton.addEventListener('click', function () {

        var query = { active: true, currentWindow: true };
        function callback(tabs) {
            var currentTab = tabs[0]; // there will be only one in this array
            console.log(currentTab.url); // also has properties like currentTab.id
            var currentLocation = currentTab.url;
            if (currentLocation.substring(12, 21) === "fangraphs") {
                //They clicked the fangraphs button, so they're already here?
            }
            else if (currentLocation.substring(12, 30) === "baseball-reference") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 10)
                console.log(playersStringTillEnd)
                var id = playersStringTillEnd.substring(0, playersStringTillEnd.length - 6);
                console.log(id);

                fetch("../data/bbref.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.update({
                                url: "https://www.fangraphs.com"
                            });
                        } else {

                            chrome.tabs.update({
                                url: `https://www.fangraphs.com/players/${player.name_first}-${player.name_last}/${player.key_fangraphs}/stats`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(8, 22) === "baseballsavant") {
                var locationOfPlayersString = currentLocation.indexOf('savant-player');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 14)
                console.log(playersStringTillEnd)
                var indexOfQuestionMark = playersStringTillEnd.indexOf("?");
                console.log(indexOfQuestionMark);
                var nameAndId = playersStringTillEnd.substring(0, indexOfQuestionMark);
                console.log(nameAndId);
                var id = nameAndId.substring(nameAndId.search(/\d/));
                console.log(id);

                fetch("../data/mlbam.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.update({
                                url: "https://www.fangraphs.com"
                            });
                        } else {

                            chrome.tabs.update({
                                url: `https://www.fangraphs.com/players/${player.name_first}-${player.name_last}/${player.key_fangraphs}/stats`
                            });
                        }
                    }
                    );
            }
            else {
                chrome.tabs.update({
                    url: "https://www.fangraphs.com"
                });
            }
        }
        chrome.tabs.query(query, callback);
    }, false);
    fanButton.addEventListener('contextmenu', function (ev) {
        ev.preventDefault();
        var query = { active: true, currentWindow: true };
        function callback(tabs) {
            var currentTab = tabs[0]; // there will be only one in this array
            console.log(currentTab.url); // also has properties like currentTab.id
            var currentLocation = currentTab.url;
            if (currentLocation.substring(12, 21) === "fangraphs") {
                //They clicked the fangraphs button, so they're already here?
            }
            else if (currentLocation.substring(12, 30) === "baseball-reference") {
                var locationOfPlayersString = currentLocation.indexOf('players');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 10)
                console.log(playersStringTillEnd)
                var id = playersStringTillEnd.substring(0, playersStringTillEnd.length - 6);
                console.log(id);

                fetch("../data/bbref.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.create({
                                url: "https://www.fangraphs.com"
                            });
                        } else {

                            chrome.tabs.create({
                                url: `https://www.fangraphs.com/players/${player.name_first}-${player.name_last}/${player.key_fangraphs}/stats`
                            });
                        }
                    }
                    );
            }
            else if (currentLocation.substring(8, 22) === "baseballsavant") {
                var locationOfPlayersString = currentLocation.indexOf('savant-player');
                console.log(locationOfPlayersString);
                var playersStringTillEnd = currentLocation.substring(locationOfPlayersString + 14)
                console.log(playersStringTillEnd)
                var indexOfQuestionMark = playersStringTillEnd.indexOf("?");
                console.log(indexOfQuestionMark);
                var nameAndId = playersStringTillEnd.substring(0, indexOfQuestionMark);
                console.log(nameAndId);
                var id = nameAndId.substring(nameAndId.search(/\d/));
                console.log(id);

                fetch("../data/mlbam.json")
                    .then(response => response.json())
                    .then(json => {
                        var player = json[id];

                        if (player === undefined) {
                            chrome.tabs.create({
                                url: "https://www.fangraphs.com"
                            });
                        } else {

                            chrome.tabs.create({
                                url: `https://www.fangraphs.com/players/${player.name_first}-${player.name_last}/${player.key_fangraphs}/stats`
                            });
                        }
                    }
                    );
            }
            else {
                chrome.tabs.create({
                    url: "https://www.fangraphs.com"
                });
            }
        }
        chrome.tabs.query(query, callback);
        return false;
    }, false);
}, false);