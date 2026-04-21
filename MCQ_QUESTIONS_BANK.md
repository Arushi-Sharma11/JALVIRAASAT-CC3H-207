# 🎯 Quick Guide: Adding MCQ Questions

## 📝 Question Template

Copy this template to add new questions:

```javascript
{
  id: 6,  // Next sequential number
  question: "Your question here?",
  options: [
    "Option A - First choice",
    "Option B - Second choice",
    "Option C - Third choice",
    "Option D - Fourth choice"
  ],
  correct: 0,  // Index: 0=A, 1=B, 2=C, 3=D
  explanation: "Explain why this answer is correct and provide learning value.",
  xp: 50  // XP reward (usually 50)
}
```

---

## 🏦 50 Ready-to-Use Financial Questions

### 💰 Budgeting & Savings (10 Questions)

```javascript
{
  id: 6,
  question: "What is the first step in creating a budget?",
  options: ["Start saving", "Track your expenses", "Cut all spending", "Invest money"],
  correct: 1,
  explanation: "Track expenses first to understand where your money goes!",
  xp: 50
},
{
  id: 7,
  question: "How much should you save before investing?",
  options: ["Nothing", "1 month expenses", "3-6 months expenses", "1 year expenses"],
  correct: 2,
  explanation: "Build emergency fund of 3-6 months expenses before investing.",
  xp: 50
},
{
  id: 8,
  question: "What is zero-based budgeting?",
  options: [
    "Spending nothing",
    "Every rupee has a purpose",
    "Saving zero money",
    "No budget needed"
  ],
  correct: 1,
  explanation: "Zero-based budgeting means assigning every rupee a specific job!",
  xp: 50
},
{
  id: 9,
  question: "What percentage of income goes to 'wants' in 50-30-20 rule?",
  options: ["20%", "30%", "40%", "50%"],
  correct: 1,
  explanation: "30% for wants (entertainment, dining out, hobbies).",
  xp: 50
},
{
  id: 10,
  question: "Which expense is a 'need' not a 'want'?",
  options: ["Netflix subscription", "Groceries", "Designer clothes", "Gaming console"],
  correct: 1,
  explanation: "Groceries are essential needs. Entertainment is a want.",
  xp: 50
},
{
  id: 11,
  question: "What is the envelope budgeting method?",
  options: [
    "Saving in envelopes",
    "Allocating cash to categories",
    "Mailing money",
    "Digital budgeting"
  ],
  correct: 1,
  explanation: "Put cash in envelopes for each spending category to control expenses.",
  xp: 50
},
{
  id: 12,
  question: "How often should you review your budget?",
  options: ["Never", "Yearly", "Monthly", "Every 5 years"],
  correct: 2,
  explanation: "Review monthly to adjust for changing income and expenses.",
  xp: 50
},
{
  id: 13,
  question: "What is lifestyle inflation?",
  options: [
    "Rising prices",
    "Spending more as income increases",
    "Economic inflation",
    "Budget cuts"
  ],
  correct: 1,
  explanation: "Lifestyle inflation = spending more when you earn more. Avoid it!",
  xp: 50
},
{
  id: 14,
  question: "What should you do with a salary bonus?",
  options: [
    "Spend it all",
    "Save/invest 70-80%",
    "Buy luxury items",
    "Ignore it"
  ],
  correct: 1,
  explanation: "Save most of bonus money. Treat yourself with 20-30% only.",
  xp: 50
},
{
  id: 15,
  question: "What is pay yourself first?",
  options: [
    "Spend on yourself",
    "Save before spending",
    "Pay bills first",
    "Buy gifts"
  ],
  correct: 1,
  explanation: "Save money first when salary comes, then spend what's left.",
  xp: 50
}
```

---

### 💳 Credit & Debt (10 Questions)

```javascript
{
  id: 16,
  question: "What is the minimum credit score for a good loan rate?",
  options: ["600", "700", "750", "800"],
  correct: 2,
  explanation: "750+ credit score gets you best interest rates on loans.",
  xp: 50
},
{
  id: 17,
  question: "What is credit utilization ratio?",
  options: [
    "Total debt",
    "Credit used / Credit limit",
    "Monthly payment",
    "Interest rate"
  ],
  correct: 1,
  explanation: "Keep credit utilization below 30% for good credit score.",
  xp: 50
},
{
  id: 18,
  question: "Which debt should you pay off first?",
  options: [
    "Lowest balance",
    "Highest interest rate",
    "Newest debt",
    "Largest amount"
  ],
  correct: 1,
  explanation: "Pay highest interest debt first to save money (avalanche method).",
  xp: 50
},
{
  id: 19,
  question: "What happens if you only pay minimum on credit card?",
  options: [
    "Debt clears fast",
    "High interest accumulates",
    "Score improves",
    "Nothing"
  ],
  correct: 1,
  explanation: "Minimum payments mean years of debt and huge interest charges!",
  xp: 50
},
{
  id: 20,
  question: "What is a good debt-to-income ratio?",
  options: ["Below 20%", "Below 36%", "Below 50%", "Below 70%"],
  correct: 1,
  explanation: "Keep total debt payments below 36% of gross income.",
  xp: 50
},
{
  id: 21,
  question: "How long does negative info stay on credit report?",
  options: ["1 year", "3 years", "7 years", "Forever"],
  correct: 2,
  explanation: "Most negative items stay for 7 years. Pay on time!",
  xp: 50
},
{
  id: 22,
  question: "What is balance transfer?",
  options: [
    "Moving money between accounts",
    "Transferring debt to lower interest card",
    "Paying off debt",
    "Closing account"
  ],
  correct: 1,
  explanation: "Transfer high-interest debt to 0% APR card to save money.",
  xp: 50
},
{
  id: 23,
  question: "What is the snowball debt method?",
  options: [
    "Pay smallest debt first",
    "Pay highest interest first",
    "Pay nothing",
    "Consolidate all debt"
  ],
  correct: 0,
  explanation: "Snowball = pay smallest debt first for psychological wins.",
  xp: 50
},
{
  id: 24,
  question: "Should you close old credit cards?",
  options: [
    "Yes, always",
    "No, keep them open",
    "Only if unused",
    "Doesn't matter"
  ],
  correct: 1,
  explanation: "Keep old cards open to maintain credit history length.",
  xp: 50
},
{
  id: 25,
  question: "What is a secured credit card?",
  options: [
    "Card with password",
    "Card backed by deposit",
    "Premium card",
    "Business card"
  ],
  correct: 1,
  explanation: "Secured card requires deposit. Good for building credit.",
  xp: 50
}
```

---

### 📈 Investing (10 Questions)

```javascript
{
  id: 26,
  question: "What is compound interest?",
  options: [
    "Simple interest",
    "Interest on interest",
    "Bank charges",
    "Loan interest"
  ],
  correct: 1,
  explanation: "Compound interest = earning interest on your interest. Powerful!",
  xp: 50
},
{
  id: 27,
  question: "What is diversification?",
  options: [
    "Buying one stock",
    "Spreading investments across assets",
    "Saving only",
    "Day trading"
  ],
  correct: 1,
  explanation: "Don't put all eggs in one basket. Diversify to reduce risk!",
  xp: 50
},
{
  id: 28,
  question: "What is SIP in mutual funds?",
  options: [
    "Single Investment Plan",
    "Systematic Investment Plan",
    "Special Interest Plan",
    "Savings Investment Plan"
  ],
  correct: 1,
  explanation: "SIP = invest fixed amount regularly in mutual funds.",
  xp: 50
},
{
  id: 29,
  question: "What is the rule of 72?",
  options: [
    "Retirement age",
    "Years to double money = 72/interest rate",
    "Investment limit",
    "Tax rule"
  ],
  correct: 1,
  explanation: "At 8% return, money doubles in 72/8 = 9 years!",
  xp: 50
},
{
  id: 30,
  question: "What is asset allocation?",
  options: [
    "Buying assets",
    "Dividing money between stocks/bonds/cash",
    "Selling assets",
    "Real estate only"
  ],
  correct: 1,
  explanation: "Asset allocation = how you split investments (60% stocks, 40% bonds).",
  xp: 50
},
{
  id: 31,
  question: "What is a mutual fund?",
  options: [
    "Bank account",
    "Pool of money from many investors",
    "Insurance policy",
    "Loan type"
  ],
  correct: 1,
  explanation: "Mutual fund pools money from investors to buy diversified assets.",
  xp: 50
},
{
  id: 32,
  question: "What is index fund?",
  options: [
    "Active trading fund",
    "Fund that tracks market index",
    "High-risk fund",
    "Savings account"
  ],
  correct: 1,
  explanation: "Index fund passively tracks Nifty/Sensex. Low fees, good returns!",
  xp: 50
},
{
  id: 33,
  question: "When should you start investing?",
  options: [
    "After retirement",
    "As soon as possible",
    "After 40",
    "Never"
  ],
  correct: 1,
  explanation: "Start early! Time in market beats timing the market.",
  xp: 50
},
{
  id: 34,
  question: "What is rupee cost averaging?",
  options: [
    "Buying at lowest price",
    "Investing fixed amount regularly",
    "Selling high",
    "Day trading"
  ],
  correct: 1,
  explanation: "Regular investing averages out market ups and downs.",
  xp: 50
},
{
  id: 35,
  question: "What is P/E ratio?",
  options: [
    "Profit/Expense",
    "Price/Earnings",
    "Portfolio/Equity",
    "Payment/EMI"
  ],
  correct: 1,
  explanation: "P/E ratio = stock price / earnings per share. Valuation metric.",
  xp: 50
}
```

---

### 🏠 Insurance & Protection (10 Questions)

```javascript
{
  id: 36,
  question: "What is term life insurance?",
  options: [
    "Investment plan",
    "Pure death benefit coverage",
    "Health insurance",
    "Car insurance"
  ],
  correct: 1,
  explanation: "Term insurance = affordable pure protection for family.",
  xp: 50
},
{
  id: 37,
  question: "How much life insurance coverage do you need?",
  options: [
    "1x annual income",
    "5x annual income",
    "10-15x annual income",
    "No insurance needed"
  ],
  correct: 2,
  explanation: "Get 10-15x annual income to protect family's future.",
  xp: 50
},
{
  id: 38,
  question: "What is health insurance deductible?",
  options: [
    "Monthly premium",
    "Amount you pay before insurance kicks in",
    "Maximum coverage",
    "Tax benefit"
  ],
  correct: 1,
  explanation: "Deductible = amount you pay first, then insurance covers rest.",
  xp: 50
},
{
  id: 39,
  question: "Should you buy insurance from employer only?",
  options: [
    "Yes, sufficient",
    "No, get additional coverage",
    "Insurance not needed",
    "Only after retirement"
  ],
  correct: 1,
  explanation: "Employer insurance ends with job. Get personal coverage too!",
  xp: 50
},
{
  id: 40,
  question: "What is critical illness insurance?",
  options: [
    "Regular health insurance",
    "Lump sum for serious diseases",
    "Life insurance",
    "Accident cover"
  ],
  correct: 1,
  explanation: "Pays lump sum if diagnosed with cancer, heart attack, etc.",
  xp: 50
},
{
  id: 41,
  question: "What is insurance premium?",
  options: [
    "Claim amount",
    "Regular payment for coverage",
    "Bonus",
    "Deductible"
  ],
  correct: 1,
  explanation: "Premium = amount you pay monthly/yearly for insurance.",
  xp: 50
},
{
  id: 42,
  question: "What is sum assured in insurance?",
  options: [
    "Premium amount",
    "Guaranteed payout amount",
    "Tax benefit",
    "Bonus"
  ],
  correct: 1,
  explanation: "Sum assured = amount insurance pays to beneficiary.",
  xp: 50
},
{
  id: 43,
  question: "Should you mix insurance with investment?",
  options: [
    "Yes, always",
    "No, keep them separate",
    "Doesn't matter",
    "Only ULIPs"
  ],
  correct: 1,
  explanation: "Buy term insurance + invest separately for better returns!",
  xp: 50
},
{
  id: 44,
  question: "What is waiting period in health insurance?",
  options: [
    "Claim processing time",
    "Time before coverage starts for certain conditions",
    "Premium payment time",
    "Policy duration"
  ],
  correct: 1,
  explanation: "Pre-existing conditions covered after waiting period (2-4 years).",
  xp: 50
},
{
  id: 45,
  question: "What is no-claim bonus in insurance?",
  options: [
    "Extra premium",
    "Discount for not claiming",
    "Penalty",
    "Tax benefit"
  ],
  correct: 1,
  explanation: "Get premium discount or higher coverage for claim-free years!",
  xp: 50
}
```

---

### 💼 Retirement & Tax (10 Questions)

```javascript
{
  id: 46,
  question: "What is PPF?",
  options: [
    "Private Pension Fund",
    "Public Provident Fund",
    "Personal Profit Fund",
    "Premium Payment Fund"
  ],
  correct: 1,
  explanation: "PPF = government savings scheme with tax benefits and guaranteed returns.",
  xp: 50
},
{
  id: 47,
  question: "At what age should you start retirement planning?",
  options: ["50", "40", "30", "As soon as you start earning"],
  correct: 3,
  explanation: "Start retirement planning from first salary. Time is your friend!",
  xp: 50
},
{
  id: 48,
  question: "What is Section 80C?",
  options: [
    "Income tax",
    "Tax deduction up to ₹1.5 lakh",
    "GST rule",
    "Property tax"
  ],
  correct: 1,
  explanation: "80C allows ₹1.5L tax deduction for PPF, ELSS, insurance, etc.",
  xp: 50
},
{
  id: 49,
  question: "What is NPS (National Pension System)?",
  options: [
    "Bank account",
    "Retirement savings scheme",
    "Insurance",
    "Loan scheme"
  ],
  correct: 1,
  explanation: "NPS = voluntary retirement savings with tax benefits.",
  xp: 50
},
{
  id: 50,
  question: "How much should you save for retirement?",
  options: [
    "10x annual expenses",
    "25-30x annual expenses",
    "5x annual expenses",
    "No specific amount"
  ],
  correct: 1,
  explanation: "Save 25-30x annual expenses for comfortable retirement.",
  xp: 50
},
{
  id: 51,
  question: "What is ELSS?",
  options: [
    "Emergency fund",
    "Equity Linked Savings Scheme",
    "Education loan",
    "Export license"
  ],
  correct: 1,
  explanation: "ELSS = tax-saving mutual fund with 3-year lock-in.",
  xp: 50
},
{
  id: 52,
  question: "What is the 4% retirement rule?",
  options: [
    "Save 4% of income",
    "Withdraw 4% of corpus annually",
    "4% interest rate",
    "Retire at 4% growth"
  ],
  correct: 1,
  explanation: "Withdraw 4% of retirement corpus yearly to make it last 30 years.",
  xp: 50
},
{
  id: 53,
  question: "What is HRA?",
  options: [
    "House Rent Allowance",
    "Health Reimbursement Account",
    "Home Repair Allowance",
    "Holiday Rental Allowance"
  ],
  correct: 0,
  explanation: "HRA = tax-exempt allowance for rent paid.",
  xp: 50
},
{
  id: 54,
  question: "What is standard deduction?",
  options: [
    "Bank charges",
    "₹50,000 automatic tax deduction for salaried",
    "Investment deduction",
    "Loan deduction"
  ],
  correct: 1,
  explanation: "₹50,000 standard deduction automatically reduces taxable income.",
  xp: 50
},
{
  id: 55,
  question: "What is EPF?",
  options: [
    "Emergency Protection Fund",
    "Employees' Provident Fund",
    "Extra Payment Fund",
    "Education Provident Fund"
  ],
  correct: 1,
  explanation: "EPF = mandatory retirement savings for salaried employees.",
  xp: 50
}
```

---

## 🚀 How to Add These Questions

### Option 1: Add All at Once
Replace the entire `questions` array in `App.jsx` with all 55 questions above.

### Option 2: Add Gradually
Add 5-10 questions at a time to keep quiz manageable.

### Option 3: Create Categories
Make separate quiz modes:
- Beginner Quiz (Questions 1-20)
- Intermediate Quiz (Questions 21-40)
- Advanced Quiz (Questions 41-55)

---

## 📝 Custom Question Checklist

When creating your own questions:

- [ ] Question is clear and specific
- [ ] 4 distinct options provided
- [ ] Only ONE correct answer
- [ ] Explanation teaches something valuable
- [ ] Appropriate difficulty level
- [ ] Relevant to daily finance
- [ ] No trick questions
- [ ] Culturally appropriate (Indian context)

---

## 🎯 Question Writing Tips

### Good Question Example ✅
```javascript
{
  question: "What is the 50-30-20 budgeting rule?",
  options: [
    "50% savings, 30% needs, 20% wants",
    "50% needs, 30% wants, 20% savings",  // Clear, specific
    "50% wants, 30% savings, 20% needs",
    "50% investments, 30% expenses, 20% fun"
  ],
  correct: 1,
  explanation: "50% for needs (rent, food), 30% for wants (entertainment), 20% for savings!"
}
```

### Bad Question Example ❌
```javascript
{
  question: "Is saving good?",  // Too vague
  options: ["Yes", "No", "Maybe", "Sometimes"],  // Not educational
  correct: 0,
  explanation: "Yes"  // No learning value
}
```

---

## 🎨 Difficulty Levels

### Easy (⭐)
- Basic definitions
- Common terms
- Simple calculations
- Beginner concepts

### Medium (⭐⭐)
- Application of concepts
- Comparisons
- Strategy questions
- Intermediate knowledge

### Hard (⭐⭐⭐)
- Complex scenarios
- Advanced strategies
- Calculations
- Expert knowledge

---

## 📊 Question Distribution

Recommended mix:
- 40% Easy questions
- 40% Medium questions
- 20% Hard questions

This keeps users engaged without frustrating them!

---

## 🔄 Update Instructions

1. Open `App.jsx`
2. Find `const questions = [...]`
3. Add new question object
4. Save file
5. Test in browser
6. Done! ✅

---

**Happy Question Creating! 🎓📚**
