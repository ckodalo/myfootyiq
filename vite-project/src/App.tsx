
import { useEffect, useState} from "react";

import './App.css'

interface Outcome {
  name: string;
  price: number;
}

interface Market {
  key: string;
  last_update: string;
  outcomes: Outcome[];
}

interface Bookmaker {
  key: string;
  title: string;
  last_update: string;
  markets: Market[];
}

interface Match {
  id: string;
  sport_key: string;
  sport_title: string;
  commence_time: string;
  home_team: string;
  away_team: string;
  bookmakers: Bookmaker[];
}

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://127.0.0.1:8000";



function App() {

   const [matches, setMatches] = useState<Match[]>([]);

  useEffect(() => {

    async function fetchOdds() {

      const response = await fetch(`${API_BASE}/odds`);

      const data: Match[] = await response.json();

      setMatches(data)
    }

    fetchOdds();
  }, []);


  return (
    <div>
      {matches.map(match => (
        <div key={match.id}>
          <h2>
            {match.home_team} vs {match.away_team}
          </h2>

          {match.bookmakers.map(bookmaker => (
            <div key={bookmaker.key}>
              <h4>{bookmaker.title}</h4>

              {bookmaker.markets[0].outcomes.map(outcome => (
                <div key={outcome.name}>
                  {outcome.name}: {outcome.price}
                </div>
              ))}
            </div>
          ))}
        </div>
      ))}
    </div>
  );

}

export default App
