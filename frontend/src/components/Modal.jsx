import React from "react";
import { useState } from "react";

function Modal({ isVisible, onClose, onSubmit, cat }) {
  //Modal is a pop up for user to submit detail info about the cat
  const [name, setName] = useState(cat.name);
  const [description, setDescription] = useState(cat.description);
  const [breed, setBreed] = useState(cat.breed);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ ...cat, name, description, breed});
    onClose();
  };

  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-6 max-w-sm w-full">
        <h2 className="text-xl font-semibold mb-4">Edit Cat Details</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700">Name:</label>
            <input
              type="text"
              className="mt-1 p-2 border w-full"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Breed:</label>
            <input
              type="text"
              className="mt-1 p-2 border w-full"
              value={breed}
              onChange={(e) => setBreed(e.target.value)}
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Description:</label>
            <textarea
              className="mt-1 p-2 border w-full"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
          </div>
          <div className="flex justify-end">
            <button
              type="button"
              className="mr-2 p-2 bg-gray-300 rounded"
              onClick={onClose}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="p-2 bg-blue-500 text-white rounded"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Modal;
