import React, { useState } from "react";
import { AiFillHeart, AiOutlineHeart } from "react-icons/ai";

function CatCard({ cat, onToggleFavorite, onCardClick }) {
  const [isPulsing, setIsPulsing] = useState(false);

  //To handle on click behavior for the like button
  const handleFavoriteClick = (e) => {
    //Prevent active the setModalVisible when click on like button
    e.stopPropagation();
    if (!cat.is_favorite) {
      setIsPulsing(true);
    }
    onToggleFavorite(cat.id, cat.is_favorite);

    if (!cat.is_favorite) {
      setTimeout(() => {
        setIsPulsing(false);
      }, 1000);
    }
  };

  //To handle when user click on the whole card to see detail information
  const handleCardClick = () => {
    onCardClick(cat);
  };

  return (
    <div
      className="mx-2 bg-white rounded-lg shadow-lg overflow-hidden flex flex-col justify-between h-full hover:scale-105 duration-200 cursor-pointer"
      onClick={handleCardClick}
    >
      <div className="flex flex-col items-center p-4">
        <h2 className="text-3xl font-semibold mb-2 text-center">{cat.name}</h2>
        <img
          src={cat.image_url}
          alt={cat.name}
          className="object-contain rounded max-h-64 w-full mb-4"
        />
      </div>
      <div className="p-4 flex justify-center">
        <button
          className={`flex items-center justify-center text-2xl transition-colors ${
            cat.is_favorite ? "text-red-500" : "text-gray-500"
          }`}
          onClick={handleFavoriteClick}
          aria-label={cat.is_favorite ? "Unfavorite" : "Favorite"}
        >
          {cat.is_favorite ? (
            <>
              <AiFillHeart className={`text-red-500 mr-2 ${isPulsing ? "pulse" : ""}`} />
              <span className="w-12 text-center text-gray-800">Liked</span>
            </>
          ) : (
            <>
              <AiOutlineHeart className="text-gray-500 mr-2" />
              <span className="w-12 text-center text-gray-800">Like</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}

export default CatCard;
