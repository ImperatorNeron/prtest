function initializeTabs(tabs, names) {
    let lastActiveTab = tabs[1];
    let lastActiveTabInfo = tabs[3];
    tabs[0].forEach((tab, index) => {
        tab.addEventListener("click", function () {
            lastActiveTab.classList.remove(names[1]);
            lastActiveTabInfo.classList.remove(names[3]);
            tabs[0][index].classList.add(names[1]);
            tabs[2][index].classList.add(names[3]);
            lastActiveTab = tabs[0][index];
            lastActiveTabInfo = tabs[2][index];
        });
    });
}

function getTabs(names) {
    return [
        document.querySelectorAll(`.${names[0]}`),
        document.querySelector(`.${names[1]}`),
        document.querySelectorAll(`.${names[2]}`),
        document.querySelector(`.${names[3]}`)
    ];
}

const first_names = ["tab", "active-tab", "tab-info", "tab-info-active"];
const first_tabs = getTabs(first_names);
initializeTabs(first_tabs, first_names);

const second_names = ["second-tab", "second-active-tab", "second-tab-info", "second-tab-info-active"];
const second_tabs = getTabs(second_names);
initializeTabs(second_tabs, second_names);
