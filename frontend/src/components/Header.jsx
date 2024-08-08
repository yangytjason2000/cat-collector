import { useState } from 'react';

const Header = ({ onApplySearch }) => {
  const [breed, setBreed] = useState('');

  const handleSubmit = () => {
    onApplySearch(breed);
  };

  return (
    <div className="flex justify-between items-center h-24">
      <h1 className="text-3xl font-bold text-center ml-8">Cat Collector</h1>
      <div className="mr-8 flex justify-center items-center">
        <label className="text-2xl font-bold text-center mx-3">Breed: </label>
        <input
          type="text"
          className="p-2 border w-full rounded-lg"
          value={breed}
          onChange={(e) => setBreed(e.target.value)}
        />
        <button
          className="ml-3 p-2 bg-blue-500 text-white rounded-lg text center"
          onClick={handleSubmit}
        >
          Search
        </button>
      </div>
    </div>
  );
};

export default Header;
