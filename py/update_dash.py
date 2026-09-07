import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        old_str = """            renderDashboard() {
                const latestRace = [...this.data.races].sort((a, b) => {
                    const d1 = new Date(a.date); const d2 = new Date(b.date);
                    if (isNaN(d1)) return 1; if (isNaN(d2)) return -1;
                    return d2 - d1;
                })[0] || this.data.races[this.data.races.length - 1];"""
                
        new_str = """            renderDashboard() {
                const sortedRaces = [...this.data.races].sort((a, b) => {
                    const d1 = new Date(a.date); const d2 = new Date(b.date);
                    if (isNaN(d1)) return 1; if (isNaN(d2)) return -1;
                    return d2 - d1;
                });
                
                if (typeof this.dashboardRaceIndex === 'undefined') {
                    this.dashboardRaceIndex = 0;
                }
                
                const latestRace = sortedRaces[this.dashboardRaceIndex] || sortedRaces[0];
                
                window.prevDashboardRace = () => {
                    if (App.dashboardRaceIndex < sortedRaces.length - 1) {
                        App.dashboardRaceIndex++;
                        App.renderDashboard();
                    }
                };
                
                window.nextDashboardRace = () => {
                    if (App.dashboardRaceIndex > 0) {
                        App.dashboardRaceIndex--;
                        App.renderDashboard();
                    }
                };"""

        content = content.replace(old_str, new_str)
        
        # Now change the header of the results
        old_header = """<h4 style="margin-bottom: 10px; font-size: 1rem; color: var(--primary);">Latest Race Results</h4>"""
        
        new_header = """<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <h4 style="font-size: 1rem; color: var(--primary); margin: 0;">Race Results</h4>
                            <div style="display: flex; gap: 10px;">
                                <button onclick="window.prevDashboardRace()" style="padding: 5px 10px; border: none; border-radius: 4px; background: var(--primary); color: white; cursor: pointer; opacity: ${App.dashboardRaceIndex >= sortedRaces.length - 1 ? 0.5 : 1}" ${App.dashboardRaceIndex >= sortedRaces.length - 1 ? 'disabled' : ''}><i class="fa-solid fa-chevron-left"></i> Prev</button>
                                <button onclick="window.nextDashboardRace()" style="padding: 5px 10px; border: none; border-radius: 4px; background: var(--primary); color: white; cursor: pointer; opacity: ${App.dashboardRaceIndex <= 0 ? 0.5 : 1}" ${App.dashboardRaceIndex <= 0 ? 'disabled' : ''}>Next <i class="fa-solid fa-chevron-right"></i></button>
                            </div>
                        </div>"""
        
        content = content.replace(old_header, new_header)
        
        # Update "Latest champion" to dynamic
        old_champion = """<span class="eyebrow">Latest champion</span>"""
        new_champion = """<span class="eyebrow">${this.dashboardRaceIndex === 0 ? 'Latest champion' : 'Champion'}</span>"""
        content = content.replace(old_champion, new_champion)

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Updated dashboard rendering logic successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
