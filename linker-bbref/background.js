// Context Menu Search
const CONTEXT_MENU_ID = "Baseball Reference context menu";
function searchText(info){
	var s = info.selectionText.toUpperCase()	;

	fetch("./fullname.json")
		.then(response => response.json())
		.then(json => {
			var player = json[s];

			if (player) {
				var lastName = player.name_last.toLowerCase();
				var initial = lastName[0];
				chrome.tabs.create({
					url: `https://www.baseball-reference.com/players/${initial}/${player.key_bbref}.shtml`
				});	
			}
		}
	);		
}
chrome.contextMenus.create({
  title: "Go to \"%s\" on Baseball Reference",
  contexts:["selection"], 
  id: CONTEXT_MENU_ID
});
chrome.contextMenus.onClicked.addListener(searchText)

// Omnibox Search
// Derived from OmniWiki (github.com/hamczu/OmniWiki)

//On Enter press, goes to baseball reference site
chrome.omnibox.onInputEntered.addListener(function(text) {
	var s = text.toUpperCase();

	fetch("./fullname.json")
        .then(response => response.json())
        .then(json => {
            var player = json[s];

			if (player) {
				var lastName = player.name_last.toLowerCase();
                var initial = lastName[0];
				chrome.tabs.create({
                    url: `https://www.baseball-reference.com/players/${initial}/${player.key_bbref}.shtml`
				});
			}
        }
	);
});
