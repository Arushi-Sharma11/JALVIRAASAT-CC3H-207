import React, { useState, useEffect } from 'react';
import { Home, Wallet, BookOpen, Gift, Zap, Trophy, PlayCircle, Lock, AlertCircle, CheckCircle, XCircle, Brain, Flame } from 'lucide-react';

// --- 1. Home Page Component ---
const HomePage = ({ data }) => {
  if (!data) return <div className="p-10 text-center font-bold">Loading Dashboard...</div>;

  return (
    <div className="p-5 pb-24 animate-in fade-in duration-500">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-2xl font-bold text-blue-800 tracking-tight">Hello, {data.name}! 👋</h1>
          <p className="text-gray-400 text-xs font-bold uppercase tracking-widest mt-1">{data.status}</p>
        </div>
        <div className="bg-yellow-100 px-3 py-1.5 rounded-2xl text-yellow-600 flex items-center gap-2 border border-yellow-200 shadow-sm">
          <Zap size={18} fill="currentColor"/> 
          <span className="font-bold text-lg">{data.xp}</span>
        </div>
      </div>

      {/* Advice Box */}
      <div className="bg-blue-50 p-4 rounded-[24px] border-l-4 border-blue-500 mb-6 flex items-start gap-3 shadow-sm">
        <AlertCircle size={20} className="text-blue-500 mt-0.5" />
        <div>
          <p className="text-[10px] font-black text-blue-500 uppercase tracking-tighter">AI Coach Advice</p>
          <p className="text-sm text-blue-900 font-medium italic mt-1 leading-snug">
            "{data.latest_advice}"
          </p>
        </div>
      </div>

      {/* Balance Card */}
      <div className="bg-gradient-to-br from-indigo-600 via-blue-600 to-blue-500 rounded-[35px] p-8 text-white shadow-2xl mb-8 relative overflow-hidden">
        <p className="opacity-70 text-xs font-bold uppercase tracking-widest">Available Balance</p>
        <h2 className="text-5xl font-black mt-2">₹{data.balance.toLocaleString()}</h2>
        <div className="absolute -bottom-6 -right-6 w-32 h-32 bg-white/10 rounded-full blur-2xl"></div>
      </div>

      {/* Financial Score Bar */}
      <div className="bg-white p-6 rounded-[30px] shadow-sm border border-gray-100">
        <div className="flex justify-between items-end mb-3">
           <h3 className="font-bold text-gray-700">Financial Health</h3>
           <span className="text-blue-600 font-black text-xl">{data.financial_score}%</span>
        </div>
        <div className="w-full bg-gray-100 h-4 rounded-full overflow-hidden p-1">
          <div 
            className={`h-full rounded-full transition-all duration-1000 ${data.financial_score > 70 ? 'bg-green-500' : data.financial_score > 40 ? 'bg-blue-500' : 'bg-red-500'}`} 
            style={{ width: `${data.financial_score}%` }}
          ></div>
        </div>
      </div>
    </div>
  );
};

// --- 2. Spend Page Component ---
const SpendPage = ({ onSpendSuccess }) => {
  const [amount, setAmount] = useState('');
  
  const handleSpend = async () => {
    if (!amount || amount <= 0) return alert("Sahi amount daalein!");
    try {
      const res = await fetch('http://127.0.0.1:8000/spend/ali_farmer', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ amount: parseInt(amount) })
      });
      const data = await res.json();
      if (data.message === "Success") {
        alert(`Transaction Success! \n\n💡 Advice: ${data.advice}`);
        onSpendSuccess(); // Home data refresh karega
      } else { alert(data.error); }
    } catch (e) { alert("Backend connect nahi ho raha!"); }
  };

  return (
    <div className="p-8 pb-24 animate-in zoom-in duration-300 text-center">
      <h2 className="text-3xl font-black text-gray-800 mb-10 tracking-tighter">ADD EXPENSE</h2>
      <div className="bg-white rounded-[50px] p-12 shadow-2xl border-4 border-blue-50 mb-10 group transition-all focus-within:border-blue-400">
        <span className="text-gray-300 font-bold block mb-2 uppercase text-xs">Enter Amount</span>
        <input 
          type="number" value={amount} onChange={(e) => setAmount(e.target.value)}
          placeholder="0" className="text-7xl font-black text-center w-full focus:outline-none text-blue-600 placeholder-gray-100" 
        />
      </div>
      <button onClick={handleSpend} className="w-full bg-blue-600 text-white py-6 rounded-[30px] font-black text-xl shadow-xl active:scale-95 transition-all uppercase tracking-widest">
        Confirm Payment
      </button>
    </div>
  );
};

// --- 3. Learn Page Component (MCQ Quiz) ---
const LearnPage = ({ onComplete }) => {
  const [quizStarted, setQuizStarted] = useState(false);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [showResult, setShowResult] = useState(false);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [answered, setAnswered] = useState(false);

  const questions = [
    {
      id: 1,
      question: "What is the 50-30-20 budgeting rule?",
      options: [
        "50% savings, 30% needs, 20% wants",
        "50% needs, 30% wants, 20% savings",
        "50% wants, 30% savings, 20% needs",
        "50% investments, 30% expenses, 20% fun"
      ],
      correct: 1,
      explanation: "50% for needs (rent, food), 30% for wants (entertainment), 20% for savings!",
      xp: 50
    },
    {
      id: 2,
      question: "How many months of expenses should your emergency fund cover?",
      options: ["1-2 months", "3-6 months", "12 months", "No need for emergency fund"],
      correct: 1,
      explanation: "Experts recommend 3-6 months of expenses for financial security.",
      xp: 50
    },
    {
      id: 3,
      question: "What is a good credit score range in India?",
      options: ["300-500", "500-650", "650-750", "750-900"],
      correct: 3,
      explanation: "750+ is excellent! It helps you get loans at lower interest rates.",
      xp: 50
    },
    {
      id: 4,
      question: "Which investment has the highest risk but potentially highest returns?",
      options: ["Fixed Deposit", "Gold", "Stocks/Equity", "Savings Account"],
      correct: 2,
      explanation: "Stocks offer high returns but come with higher risk. Diversify your portfolio!",
      xp: 50
    },
    {
      id: 5,
      question: "What does EMI stand for?",
      options: [
        "Easy Money Investment",
        "Equated Monthly Installment",
        "Extra Money Income",
        "Emergency Money Insurance"
      ],
      correct: 1,
      explanation: "EMI = Equated Monthly Installment. It's how you repay loans in equal parts.",
      xp: 50
    }
  ];

  const handleAnswer = (index) => {
    if (answered) return;
    setSelectedAnswer(index);
    setAnswered(true);

    const isCorrect = index === questions[currentQuestion].correct;
    if (isCorrect) {
      setScore(score + 1);
      setStreak(streak + 1);
    } else {
      setStreak(0);
    }
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer(null);
      setAnswered(false);
    } else {
      setShowResult(true);
    }
  };

  const handleFinish = async () => {
    const totalXP = score * 50 + (streak >= 3 ? 100 : 0);
    const res = await fetch('http://127.0.0.1:8000/add_xp/ali_farmer', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ points: totalXP })
    });
    await res.json();
    onComplete();
    alert(`🎉 Quiz Complete! +${totalXP} XP earned!\n\nScore: ${score}/${questions.length}`);
    setQuizStarted(false);
    setCurrentQuestion(0);
    setScore(0);
    setStreak(0);
    setShowResult(false);
  };

  if (!quizStarted) {
    return (
      <div className="p-6 pb-24 animate-in slide-in-from-right-4">
        <div className="text-center mb-8">
          <Brain size={60} className="text-purple-500 mx-auto mb-4" />
          <h2 className="text-3xl font-black text-gray-800">Financial Quiz</h2>
          <p className="text-gray-500 mt-2">Test your money knowledge!</p>
        </div>

        <div className="bg-gradient-to-br from-purple-500 to-pink-500 rounded-[35px] p-8 text-white mb-6 shadow-xl">
          <h3 className="text-2xl font-black mb-4">🎯 Challenge Yourself</h3>
          <div className="space-y-3 text-sm">
            <div className="flex items-center gap-3">
              <CheckCircle size={20} />
              <span>5 Questions on Financial Literacy</span>
            </div>
            <div className="flex items-center gap-3">
              <Zap size={20} fill="white" />
              <span>Earn 50 XP per correct answer</span>
            </div>
            <div className="flex items-center gap-3">
              <Flame size={20} fill="white" />
              <span>Bonus +100 XP for 3+ streak</span>
            </div>
          </div>
        </div>

        <button 
          onClick={() => setQuizStarted(true)} 
          className="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-6 rounded-[30px] font-black text-xl shadow-xl active:scale-95 transition-all"
        >
          START QUIZ 🚀
        </button>
      </div>
    );
  }

  if (showResult) {
    const totalXP = score * 50 + (streak >= 3 ? 100 : 0);
    const percentage = (score / questions.length) * 100;

    return (
      <div className="p-6 pb-24 text-center animate-in zoom-in">
        <Trophy size={80} className="text-yellow-500 mx-auto mb-6" />
        <h2 className="text-3xl font-black text-gray-800 mb-4">Quiz Complete!</h2>
        
        <div className="bg-white rounded-[35px] p-8 shadow-xl mb-6">
          <div className="text-6xl font-black text-blue-600 mb-2">{score}/{questions.length}</div>
          <p className="text-gray-500 font-bold">Correct Answers</p>
          <div className="mt-6 pt-6 border-t border-gray-100">
            <div className="flex justify-around text-center">
              <div>
                <div className="text-3xl font-black text-purple-600">+{totalXP}</div>
                <div className="text-xs text-gray-500 font-bold">XP EARNED</div>
              </div>
              <div>
                <div className="text-3xl font-black text-orange-600">{percentage}%</div>
                <div className="text-xs text-gray-500 font-bold">ACCURACY</div>
              </div>
            </div>
          </div>
        </div>

        {percentage >= 80 && (
          <div className="bg-green-50 border-2 border-green-200 rounded-2xl p-4 mb-6">
            <p className="text-green-700 font-bold">🌟 Excellent! You're a finance pro!</p>
          </div>
        )}

        <button 
          onClick={handleFinish} 
          className="w-full bg-blue-600 text-white py-6 rounded-[30px] font-black text-xl shadow-xl active:scale-95"
        >
          CLAIM REWARDS
        </button>
      </div>
    );
  }

  const q = questions[currentQuestion];
  const isCorrect = selectedAnswer === q.correct;

  return (
    <div className="p-6 pb-24 animate-in fade-in">
      {/* Header */}
      <div className="flex justify-between items-center mb-6">
        <div className="bg-blue-100 px-4 py-2 rounded-full">
          <span className="text-blue-600 font-black text-sm">
            Question {currentQuestion + 1}/{questions.length}
          </span>
        </div>
        <div className="flex items-center gap-2">
          <Flame size={20} className="text-orange-500" fill={streak > 0 ? "#f97316" : "none"} />
          <span className="font-black text-orange-600">{streak} 🔥</span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-gray-200 h-2 rounded-full mb-8">
        <div 
          className="bg-gradient-to-r from-purple-500 to-pink-500 h-full rounded-full transition-all duration-500"
          style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
        ></div>
      </div>

      {/* Question Card */}
      <div className="bg-white rounded-[35px] p-8 shadow-xl mb-6">
        <h3 className="text-xl font-black text-gray-800 mb-6 leading-snug">{q.question}</h3>
        
        <div className="space-y-3">
          {q.options.map((option, index) => {
            let bgColor = 'bg-gray-50 border-2 border-gray-200';
            let textColor = 'text-gray-800';
            let icon = null;

            if (answered) {
              if (index === q.correct) {
                bgColor = 'bg-green-100 border-2 border-green-500';
                textColor = 'text-green-700';
                icon = <CheckCircle size={20} className="text-green-500" />;
              } else if (index === selectedAnswer) {
                bgColor = 'bg-red-100 border-2 border-red-500';
                textColor = 'text-red-700';
                icon = <XCircle size={20} className="text-red-500" />;
              }
            }

            return (
              <button
                key={index}
                onClick={() => handleAnswer(index)}
                disabled={answered}
                className={`w-full p-4 rounded-2xl font-bold text-left transition-all active:scale-95 flex items-center justify-between ${bgColor} ${textColor}`}
              >
                <span>{option}</span>
                {icon}
              </button>
            );
          })}
        </div>
      </div>

      {/* Explanation */}
      {answered && (
        <div className={`p-6 rounded-[25px] mb-6 animate-in slide-in-from-bottom ${isCorrect ? 'bg-green-50 border-l-4 border-green-500' : 'bg-orange-50 border-l-4 border-orange-500'}`}>
          <p className="font-bold text-sm mb-2 uppercase tracking-wide">
            {isCorrect ? '✅ Correct!' : '💡 Learn This'}
          </p>
          <p className="text-gray-700">{q.explanation}</p>
          <div className="mt-3 text-sm font-black text-purple-600">+{isCorrect ? q.xp : 0} XP</div>
        </div>
      )}

      {/* Next Button */}
      {answered && (
        <button 
          onClick={handleNext}
          className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white py-5 rounded-[30px] font-black text-lg shadow-xl active:scale-95 transition-all"
        >
          {currentQuestion < questions.length - 1 ? 'NEXT QUESTION →' : 'SEE RESULTS 🎉'}
        </button>
      )}
    </div>
  );
};

// --- 4. Rewards Page Component ---
const RewardsPage = ({ xp, onRedeem }) => {
  const coupons = [
    { id: 1, brand: "Zomato", cost: 300, icon: "🍕", gift: "20% OFF" },
    { id: 2, brand: "Amazon", cost: 500, icon: "📦", gift: "₹100 Card" }
  ];

  const handleRedeem = async (c) => {
    if (xp < c.cost) return alert("Pehle padhai karo, XP kam hain!");
    const res = await fetch('http://127.0.0.1:8000/redeem/ali_farmer', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ cost: c.cost, brand: c.brand })
    });
    const d = await res.json();
    if (d.message === "Success") { onRedeem(); alert(`${c.brand} coupon unlock ho gaya!`); }
  };

  return (
    <div className="p-5 pb-24">
      <div className="bg-yellow-400 rounded-[35px] p-8 text-center text-white mb-8 shadow-lg shadow-yellow-200">
        <Trophy size={48} className="mx-auto mb-3" />
        <h2 className="text-5xl font-black">{xp}</h2>
        <p className="font-bold opacity-80 uppercase text-xs tracking-widest mt-1">Total XP Points</p>
      </div>
      <div className="space-y-4">
        {coupons.map(c => (
          <div key={c.id} className={`p-6 rounded-[30px] flex justify-between items-center transition-all ${xp >= c.cost ? 'bg-white shadow-md border-2 border-green-100' : 'bg-gray-50 opacity-50'}`}>
            <div className="flex items-center gap-5">
               <div className="text-4xl bg-gray-50 w-16 h-16 flex items-center justify-center rounded-2xl">{c.icon}</div>
               <div><p className="font-black text-gray-800">{c.brand}</p><p className="text-xs text-blue-600 font-bold">{c.gift}</p></div>
            </div>
            <button onClick={() => handleRedeem(c)} className={`px-6 py-3 rounded-2xl font-black text-xs ${xp >= c.cost ? 'bg-black text-white shadow-lg active:scale-95' : 'bg-gray-200 text-gray-400'}`}>
              {xp >= c.cost ? "GET IT" : <Lock size={16}/>}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

// --- MAIN APP COMPONENT ---
export default function App() {
  const [page, setPage] = useState('home');
  const [userData, setUserData] = useState(null);

  const fetchData = () => {
    fetch('http://127.0.0.1:8000/user/ali_farmer')
      .then(res => res.json())
      .then(data => setUserData(data));
  };

  useEffect(() => { fetchData(); }, []);

  if (!userData) return (
    <div className="h-screen flex flex-col items-center justify-center bg-blue-600 text-white">
      <Zap size={50} className="animate-bounce mb-4" />
      <h1 className="text-2xl font-black uppercase tracking-widest">FIN-APP AI</h1>
    </div>
  );

  return (
    <div className="max-w-md mx-auto bg-gray-50 min-h-screen relative shadow-2xl overflow-hidden font-sans border-x border-gray-200">
      {page === 'home' && <HomePage data={userData} />}
      {page === 'spend' && <SpendPage onSpendSuccess={() => { fetchData(); setPage('home'); }} />}
      {page === 'learn' && <LearnPage onComplete={fetchData} />}
      {page === 'rewards' && <RewardsPage xp={userData.xp} onRedeem={fetchData} />}

      {/* Bottom Navbar */}
      <div className="fixed bottom-0 w-full max-w-md bg-white/95 backdrop-blur-md border-t border-gray-100 flex justify-around py-5 rounded-t-[40px] shadow-[0_-10px_40px_rgba(0,0,0,0.05)] z-50">
        <NavBtn icon={<Home/>} active={page==='home'} onClick={() => setPage('home')} />
        <NavBtn icon={<Wallet/>} active={page==='spend'} onClick={() => setPage('spend')} />
        <NavBtn icon={<BookOpen/>} active={page==='learn'} onClick={() => setPage('learn')} />
        <NavBtn icon={<Gift/>} active={page==='rewards'} onClick={() => setPage('rewards')} />
      </div>
    </div>
  );
}

const NavBtn = ({ icon, active, onClick }) => (
  <button onClick={onClick} className={`p-3 rounded-2xl transition-all duration-300 ${active ? 'bg-blue-600 text-white scale-110 shadow-lg shadow-blue-200' : 'text-gray-400 hover:text-gray-600'}`}>
    {React.cloneElement(icon, { size: 24, strokeWidth: 3 })}
  </button>
);