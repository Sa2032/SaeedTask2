import React, { useState } from 'react';
import paper from './paper.svg';
import rock from './Rock.svg';
import scissors from './scissors.svg';
import shadow from './shadow.svg';
import './App.css';

function App() {
  const [result, setResult] = useState('Choose:');
  const [playerChoice, setPlayerChoice] = useState('');
  const [computerChoice, setComputerChoice] = useState('');

  const choices = ['rock', 'paper', 'scissors'];
  const choiceImages = {
    rock: rock,
    paper: paper,
    scissors: scissors,
  };

  const getRandomChoice = () => {
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
  };

  const handleClick = (playerSelection) => {
    const computerSelection = getRandomChoice();
    setPlayerChoice(playerSelection);
    setComputerChoice(computerSelection);

    if (playerSelection === computerSelection) {
      setResult('YOU TIED!');
    } else if (
      (playerSelection === 'rock' && computerSelection === 'scissors') ||
      (playerSelection === 'paper' && computerSelection === 'rock') ||
      (playerSelection === 'scissors' && computerSelection === 'paper')
    ) {
      setResult('YOU WIN!');
    } else {
      setResult('YOU LOST!');
    }
  };

  return (
    <div className="App">
      <p className="Text">{result}</p>
      {!playerChoice && !computerChoice && (
        <div className="App-header">
        <div onClick={() => handleClick('rock')} className="choice-image-rock choice-image">
          <div className="image-container-x">
            <img src={rock} alt="Rock" className="choice-img" />
            <img src={shadow} alt="Rock-shadow" className="rock-shadow" />
          </div>
        </div>
        <div onClick={() => handleClick('paper')} className="choice-image-paper choice-image">
          <div className="image-container-x">
            <img src={paper} alt="Paper" className="choice-img" />
            <img src={shadow} alt="Paper-shadow" className="paper-shadow" />
          </div>
        </div>
        <div onClick={() => handleClick('scissors')} className="choice-image-scissors choice-image">
          <div className="image-container-x">
            <img src={scissors} alt="Scissors" className="choice-img" />
            <img src={shadow} alt="Scissors-shadow" className="scissors-shadow" />
          </div>
        </div>
      </div>
      
      )}
      {playerChoice && computerChoice && (
        <div className="Results-container">
        <div className="Result-item">
          <div className="image-container">
            <img src={choiceImages[playerChoice]} alt={playerChoice} className="result-image" />
            <img src={shadow} alt={playerChoice} className="shadow" />
          </div>
        </div>
        <div className="Result-item">
          <div className="image-container">
            <img src={choiceImages[computerChoice]} alt={computerChoice} style={{ transform: "scaleX(-1)" }} className="result-image" />
            <img src={shadow} alt={computerChoice} className="shadow" />
          </div>
        </div>
      </div>
      
      )}
    </div>
  );
}

export default App;
