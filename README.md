# BESTEM-2025

This repo tracks our team's (**beERror**) progress throught the BESTEM 2025 hackathon.

## A game where:

1. The system provides a **word each round** (e.g., *Tornado, Hammer, Pandemic*).
2. The player must **choose a word** from a **predefined list** that "beats" the system's word.
3. Every word the player picks has a **cost ($)** — stronger words are more expensive.
4. If the player **fails to beat** the system’s word, they incur a **penalty**.
5. The game lasts **10 rounds**.
6. **Lowest total cost wins**, factoring in **win discounts** and **smart-play bonuses**!

## How the Game Works

1. **System generates a word** (e.g., *Flood*).
2. **Player selects a word** from the predefined list (e.g., *Drought*).
3. **The game checks** if the player's word “beats” the system’s word:
    - ✅ **Win**: Only the word’s cost is deducted.
    - ❌ **Loss**: The word’s cost + a penalty are deducted.
4. **Players play simultaneously** in each round.
5. **Repeat for 10 rounds**.
6. After 10 rounds, **final scores are calculated** with **special discounts and bonuses**.

## The Rules

### 1️⃣ The Words

- **System words** are randomly chosen from a secret list.
- **Player words** come from a **fixed 77-word list**, each with an associated cost.

### 2️⃣ Choosing a Word

- Players can **only select from the predefined list**.
- Players **don’t know the system’s full word list**, so they must think strategically.

### 3️⃣ Winning & Losing a Round

- A player’s word must **logically beat** the system’s word.
- If successful:
✅ The **word’s cost is deducted**, and the round continues.
- If unsuccessful:
❌ A **penalty fee** is deducted in addition to the word’s cost. 
- Game End & Scoring
5% Discount per Round Won:
After 10 rounds, you receive 5% off your total bill for every round you won.
(e.g., win 7 rounds → 35% discount.)
The final score = total money spent (cost of words + penalties).
Cheaper Win Bonus:
If both players beat the system word, the player who spent less gets a 20% refund of their word's cost for that round.
Final Score Formula:
Final Cost = ((Total Spent + 75 * Rounds Lost)  × (1 - (5% × Rounds Won))) - (Sum of Cheaper Win Refunds).