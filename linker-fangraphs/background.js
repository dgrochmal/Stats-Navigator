// Context Menu Search
const CONTEXT_MENU_ID = "Fangraphs context menu";
function searchText(info){
	var s = info.selectionText.toUpperCase();

	fetch("./fullname.json")
	.then(response => response.json())
	.then(json => {
		var player = json[s];

		if (player) {
			chrome.tabs.create({url: `https://www.fangraphs.com/players/${player.name_first}-${player.name_last}/${player.key_fangraphs}/stats`});	
		}
	}
	);
}
chrome.contextMenus.create({
  title: "Go to \"%s\" on Fangraphs",
  contexts:["selection"], 
  id: CONTEXT_MENU_ID
});
chrome.contextMenus.onClicked.addListener(searchText)

// Omnibox Search
// Derived from OmniWiki (github.com/hamczu/OmniWiki)

//On Enter press, goes to fangraphs site
chrome.omnibox.onInputEntered.addListener(function(text) {
	var s = text.toUpperCase();

	fetch("./fullname.json")
	.then(response => response.json())
	.then(json => {
		var player = json[s];

		if (player) {
			chrome.tabs.create({url: `https://www.fangraphs.com/players/${player.name_first}-${player.name_last}/${player.key_fangraphs}/stats`});	
		}
	}
	);
});
