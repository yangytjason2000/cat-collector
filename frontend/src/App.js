import { useEffect, useState} from "react";
import axios from 'axios';
import CatCard from "./components/CatCard";
import InfiniteScroll from 'react-infinite-scroll-component';
import Modal from "./components/Modal";

function App() {
  const [catsData, setCatsData] = useState([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [selectedCat, setSelectedCat] = useState(null);

  //initial page load
  useEffect(() => {
    loadCats(page);
  }, [page]);

  //Fetch data from the backend for a given page
  const loadCats = (page) => {
    axios
      .get(`http://localhost:5000/cats`, { params: { page, limit: 10 } })
      .then((response) => {
        const newCats = response.data;
        setCatsData((prevCats) => [...prevCats, ...newCats]);
        setHasMore(newCats.length > 0);
      })
      .catch((error) => {
        console.error('Error fetching cat data:', error);
      });
  };

  //Use by inifite scroll to fetch next page
  const fetchMoreData = () => {
    setPage(prevPage => prevPage + 1);
  };

  //Update user favorite status for a give cat id
  const toggleFavorite = (catId, isFavorite) => {
    const endpoint = isFavorite ? `http://localhost:5000/cats/${catId}` : 'http://localhost:5000/cats';
    const request = isFavorite ? axios.delete(endpoint) : axios.post(endpoint, { cat_id: catId });

    request
      .then((response) => {
        console.log(response.data.message);
        const index = catsData.findIndex((cat) => cat.id === catId);
        if (index !== -1) {
          const updatedCats = [...catsData];
          updatedCats[index] = {
            ...updatedCats[index],
            is_favorite: !updatedCats[index].is_favorite,
          };
          setCatsData(updatedCats);
        }
      })
      .catch((error) => {
        console.error('Error updating cat favorite status:', error);
      });
  };

  //Update cat's detailed information including name and description
  const updateCat = (updatedCat) => {
    axios
      .put(`http://localhost:5000/cats/${updatedCat.id}`, {
        name: updatedCat.name,
        description: updatedCat.description,
      })
      .then((response) => {
        console.log(response.data.message);
        setCatsData((prevCats) =>
          prevCats.map((cat) =>
            cat.id === updatedCat.id ? { ...cat, ...updatedCat } : cat
          )
        );
      })
      .catch((error) => {
        console.error("Error updating cat details:", error);
      });
  };

  //Set the cat that need to be displayed in the pop up modal
  const handleCardClick = (cat) => {
    setSelectedCat(cat);
  };

  const handleModalClose = () => {
    setSelectedCat(null);
  };

  return (
    <div className="bg-slate-400 min-h-screen w-full">
      <h1 className="text-3xl font-bold underline text-center">Cat Collector</h1>
      <InfiniteScroll
        dataLength={catsData.length}
        next={fetchMoreData}
        hasMore={hasMore}
        loader={<h4 className="text-2xl font-bold text-center">Loading...</h4>}
        endMessage={
          <p className="text-2xl font-bold text-center">
            <b>No more cats...</b>
          </p>
        }
      >
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-16 p-4">
          {catsData.map((cat) => (
            <CatCard
              key={cat.id}
              cat={cat}
              onToggleFavorite={toggleFavorite}
              onCardClick={handleCardClick}
            />
          ))}
        </div>
      </InfiniteScroll>
      {selectedCat && (
        <Modal
          isVisible={true}
          onClose={handleModalClose}
          onSubmit={updateCat}
          cat={selectedCat}
        />
      )}
    </div>
  );
}

export default App;
