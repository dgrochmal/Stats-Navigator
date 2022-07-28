// Context Menu Search
const CONTEXT_MENU_ID = "Baseball Savant context menu";
function searchText(info){
	var s = info.selectionText.toUpperCase();

	fetch("./fullname.json")
		.then(response => response.json())
		.then(json => {
			var player = json[s];

			if (player) {
				chrome.tabs.create({url: `https://baseballsavant.mlb.com/savant-player/${player.name_first}-${player.name_last}-${player.key_mlbam}`});
			}
		}
	);
}
chrome.contextMenus.create({
  title: "Go to \"%s\" on Baseball Savant",
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
				chrome.tabs.create({url: `https://baseballsavant.mlb.com/savant-player/${player.name_first}-${player.name_last}-${player.key_mlbam}`});
			}
		}
		);
});
