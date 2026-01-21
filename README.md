# 🐍 Python Interview — Q & A

## Table of Contents

- [🐍 Python Interview — Q \& A](#-python-interview--q--a)
  - [Table of Contents](#table-of-contents)
  - [Core Concepts](#core-concepts)
  - [Advanced Python](#advanced-python)
- [🧮 SQL Interview — Q \& A](#-sql-interview--q--a)
  - [Fundamentals](#fundamentals)
  - [Advanced SQL](#advanced-sql)
- [🌐 JavaScript Interview — Q \& A](#-javascript-interview--q--a)
  - [Core Concepts](#core-concepts-1)
  - [Advanced JavaScript](#advanced-javascript)
- [🧠 General Programming — Q \& A](#-general-programming--q--a)
- [🧱 System Design — Q \& A](#-system-design--q--a)
- [🧪 Practical / Behavioral — Q \& A](#-practical--behavioral--q--a)
- [⚡ Strong-Signal Questions — Q \& A](#-strong-signal-questions--q--a)
- [🧪 Flask Interview — Q \& A](#-flask-interview--q--a)
  - [Core Concepts](#core-concepts-2)
  - [Advanced Flask](#advanced-flask)
- [⚛️ React Interview — Q \& A](#️-react-interview--q--a)
  - [Core Concepts](#core-concepts-3)
  - [Advanced React](#advanced-react)
- [🔄 Flask + React Integration — Q \& A](#-flask--react-integration--q--a)
- [🧪 Testing — Q \& A](#-testing--q--a)
- [🚀 Deployment \& Production — Q \& A](#-deployment--production--q--a)
- [⚡ Strong-Signal Questions (Senior Level)](#-strong-signal-questions-senior-level)

---

## Core Concepts

**Q: What's the difference between a list and a tuple?**  
A: Lists are mutable, tuples are immutable. Tuples are faster, hashable, and safer for fixed data.

**Q: How does Python handle memory management?**  
A: Through reference counting and a cyclic garbage collector for circular references.

**Q: What are mutable vs immutable types?**  
A: Mutable types can change in place (list, dict, set). Immutable types create new objects when modified (int, str, tuple).

**Q: What are `*args` and `**kwargs`?**  
A: `*args` captures extra positional arguments as a tuple; `**kwargs` captures keyword arguments as a dict.

**Q: What is the GIL?**  
A: The Global Interpreter Lock ensures only one thread executes Python bytecode at a time, simplifying memory safety.

**Q: When should you use multithreading vs multiprocessing in Python?**  
A: Threads for I/O-bound tasks; multiprocessing for CPU-bound tasks to bypass the GIL.

## Advanced Python

**Q: What is a decorator?**  
A: A function that wraps another function to extend behavior without modifying its code.

**Q: Difference between `__str__` and `__repr__`?**  
A: `__str__` is user-facing; `__repr__` is developer-facing and unambiguous.

**Q: What are comprehensions?**  
A: A concise syntax for constructing collections, often faster and more readable than loops.

**Q: What happens with `a = b = []`?**  
A: Both variables reference the same list; mutations affect both.

**Q: Difference between shallow and deep copy?**  
A: Shallow copies references; deep copies recursively copy all nested objects.

**Q: Generators vs iterators?**  
A: Generators use yield and produce values lazily; iterators implement `__next__`.

**Q: What is a context manager?**  
A: An object that manages setup and teardown via `__enter__` and `__exit__`.

**Q: How does `asyncio` work?**  
A: It uses an event loop to run coroutines cooperatively in a single thread.

**Q: What is monkey patching?**  
A: Modifying code at runtime; powerful but risky.

**Q: What is MRO?**  
A: Method Resolution Order — the order Python follows to resolve inherited methods.

---

# 🧮 SQL Interview — Q & A

## Fundamentals

**Q: Difference between WHERE and HAVING?**  
A: WHERE filters rows before aggregation; HAVING filters after aggregation.

**Q: Primary key vs foreign key?**  
A: A primary key uniquely identifies a row; a foreign key references another table's primary key.

**Q: Explain SQL joins.**  
A: INNER returns matches; LEFT/RIGHT return all rows from one side; FULL returns all rows.

**Q: What is normalization?**  
A: Structuring data to reduce redundancy and improve integrity.

**Q: When would you denormalize?**  
A: For read-heavy systems where performance outweighs strict normalization.

**Q: DELETE vs TRUNCATE vs DROP?**  
A: DELETE removes rows, TRUNCATE removes all rows fast, DROP removes the table.

**Q: What is an index?**  
A: A data structure that speeds up reads at the cost of write performance and storage.

## Advanced SQL

**Q: What are window functions?**  
A: Functions that compute values across related rows without collapsing them.

**Q: What is an execution plan?**  
A: The database's strategy for executing a query.

**Q: Explain ACID.**  
A: Atomicity, Consistency, Isolation, Durability — guarantees for transactions.

**Q: What is a transaction?**  
A: A group of operations that either fully succeed or fully fail.

**Q: OLTP vs OLAP?**  
A: OLTP handles frequent small transactions; OLAP handles large analytical queries.

---

# 🌐 JavaScript Interview — Q & A

## Core Concepts

**Q: Difference between `var`, `let`, and `const`?**  
A: `var` is function-scoped; `let` and `const` are block-scoped; `const` prevents reassignment.

**Q: What is hoisting?**  
A: Declarations are moved to the top of their scope during compilation.

**Q: What is a closure?**  
A: A function that retains access to its outer scope after execution.

**Q: Explain `this`.**  
A: Its value depends on how a function is called; arrow functions inherit it.

**Q: `==` vs `===`?**  
A: `==` allows coercion; `===` enforces strict equality.

**Q: What is event bubbling vs capturing?**  
A: Bubbling moves events up the DOM; capturing moves down.

**Q: What is a promise?**  
A: An object representing a future value with pending, fulfilled, or rejected states.

**Q: What does `async/await` do?**  
A: Provides synchronous-looking syntax over promises.

## Advanced JavaScript

**Q: How does the event loop work?**  
A: It processes the call stack, then microtasks, then macrotasks.

**Q: What is prototypal inheritance?**  
A: Objects inherit properties from other objects via a prototype chain.

**Q: Debounce vs throttle?**  
A: Debounce delays execution; throttle limits execution frequency.

**Q: How does JS manage memory?**  
A: Automatic garbage collection; leaks come from lingering references.

**Q: `bind`, `call`, and `apply`?**  
A: All set `this`; `bind` returns a new function, `call`/`apply` invoke immediately.

---

# 🧠 General Programming — Q & A

**Q: When use arrays vs linked lists?**  
A: Arrays for fast access; linked lists for fast inserts/deletes.

**Q: Stack vs queue?**  
A: Stack is LIFO; queue is FIFO.

**Q: How does a hash table work?**  
A: A hash function maps keys to buckets; collisions are resolved internally.

**Q: BFS vs DFS?**  
A: BFS explores level by level; DFS explores depth-first.

**Q: What is Big-O?**  
A: A measure of algorithmic scalability.

**Q: Quicksort vs mergesort?**  
A: Quicksort is in-place and cache-friendly; mergesort is stable and predictable.

**Q: Greedy vs dynamic programming?**  
A: Greedy makes local choices; DP solves overlapping subproblems optimally.

**Q: How do you detect a cycle in a graph?**  
A: Use a visited set or Floyd's cycle detection algorithm.

---

# 🧱 System Design — Q & A

**Q: What is REST?**  
A: A stateless, resource-oriented architecture using HTTP verbs.

**Q: REST vs GraphQL?**  
A: REST has fixed endpoints; GraphQL allows flexible queries.

**Q: What is idempotency?**  
A: Multiple identical requests yield the same result.

**Q: What is eventual consistency?**  
A: Data becomes consistent over time.

**Q: What is a race condition?**  
A: Multiple actors access shared state unsafely.

**Q: What is a deadlock?**  
A: Circular waiting for resources.

**Q: How would you design a rate limiter?**  
A: Token bucket or sliding window, often Redis-backed.

**Q: How would you design a URL shortener?**  
A: Unique ID generation, persistent storage, caching, and redirects.

---

# 🧪 Practical / Behavioral — Q & A

**Q: How do you debug a production issue?**  
A: Reproduce, inspect logs/metrics, isolate, fix, and write a postmortem.

**Q: How do you approach legacy code?**  
A: Add tests first, then refactor incrementally.

**Q: What makes code testable?**  
A: Small functions, clear boundaries, dependency injection.

**Q: Unit vs integration tests?**  
A: Unit tests isolate logic; integration tests verify components together.

**Q: How do you review code?**  
A: Focus on correctness, clarity, maintainability, and edge cases.

---

# ⚡ Strong-Signal Questions — Q & A

**Q: Describe a system you built.**  
A: Focus on tradeoffs, constraints, and lessons learned.

**Q: A technical decision you regret?**  
A: Own the mistake and explain what you learned.

**Q: Performance vs readability?**  
A: Default to readability; optimize proven bottlenecks.

**Q: When do you refactor?**  
A: When change cost becomes high or complexity increases.

---

# 🧪 Flask Interview — Q & A

## Core Concepts

**Q: What is Flask?**  
A: Flask is a lightweight Python web framework designed for building web APIs and applications with minimal abstraction.

**Q: Why choose Flask over Django?**  
A: Flask offers flexibility and simplicity, while Django provides more built-in features. Flask is preferred for microservices and custom architectures.

**Q: What is WSGI?**  
A: Web Server Gateway Interface — a standard interface between Python web apps and servers.

**Q: How does request handling work in Flask?**  
A: Requests are routed via decorators, processed in view functions, and return responses.

**Q: What are Flask Blueprints?**  
A: Modular components that help organize routes, templates, and static files.

**Q: How do you handle configuration in Flask?**  
A: Via environment variables, config files, or class-based configuration objects.

**Q: How does Flask handle sessions?**  
A: Sessions are client-side, signed cookies by default.

**Q: How do you secure a Flask app?**  
A: Input validation, CSRF protection, HTTPS, auth middleware, and secret key management.

**Q: How do you manage database connections?**  
A: Typically via SQLAlchemy and application context handling.

**Q: How do Flask middlewares work?**  
A: Using `before_request`, `after_request`, and `teardown_request` hooks.

## Advanced Flask

**Q: What is Flask's application context?**  
A: It provides access to global objects like `request`, `g`, and `current_app`.

**Q: How do you implement authentication?**  
A: Using JWTs, OAuth, or Flask-Login depending on requirements.

**Q: How do you implement authorization?**  
A: Role-based access control, permission checks, or policy-based decorators.

**Q: How do you handle errors in Flask?**  
A: Custom error handlers using `@app.errorhandler`.

**Q: How do you scale a Flask app?**  
A: Run behind a WSGI server (Gunicorn), horizontal scaling, caching, and async workers.

**Q: Flask vs FastAPI?**  
A: FastAPI has built-in async support and validation; Flask is simpler and more flexible.

---

# ⚛️ React Interview — Q & A

## Core Concepts

**Q: What is React?**  
A: A JavaScript library for building declarative, component-based user interfaces.

**Q: What problem does React solve?**  
A: Managing complex UI state and keeping the UI in sync with application data.

**Q: What is JSX?**  
A: A syntax extension that allows writing HTML-like code in JavaScript.

**Q: What is a component?**  
A: A reusable UI unit that encapsulates logic, state, and rendering.

**Q: Functional vs class components?**  
A: Functional components use hooks and are now preferred; class components are legacy.

**Q: What is state?**  
A: Data that affects rendering and can change over time.

**Q: What are props?**  
A: Immutable inputs passed from parent to child components.

**Q: What are hooks?**  
A: Functions that add state and lifecycle behavior to functional components.

## Advanced React

**Q: What does `useEffect` do?**  
A: It handles side effects like data fetching, subscriptions, and DOM interactions.

**Q: What is the dependency array in `useEffect`?**  
A: It controls when the effect runs to avoid unnecessary executions.

**Q: What is lifting state up?**  
A: Moving shared state to the nearest common ancestor.

**Q: What is controlled vs uncontrolled input?**  
A: Controlled inputs are managed by React state; uncontrolled rely on the DOM.

**Q: What is the virtual DOM?**  
A: A lightweight copy of the DOM used to optimize updates.

**Q: How does React handle performance?**  
A: Reconciliation, memoization, and selective re-rendering.

**Q: What is reconciliation?**  
A: The process of diffing virtual DOM trees to update the real DOM efficiently.

---

# 🔄 Flask + React Integration — Q & A

**Q: How do Flask and React typically interact?**  
A: Flask serves as an API backend; React consumes it via HTTP (REST or GraphQL).

**Q: How do you handle authentication across Flask and React?**  
A: Using JWT tokens stored securely and sent via headers.

**Q: How do you handle CORS?**  
A: Configure Flask-CORS and restrict allowed origins and methods.

**Q: How do you structure a Flask + React project?**  
A: Separate frontend and backend repos or monorepo with clear API boundaries.

**Q: How do you handle environment variables?**  
A: `.env` files, environment-specific configs, and build-time variables in React.

**Q: How do you handle errors end-to-end?**  
A: Standardized API error responses and frontend error boundaries.

**Q: How do you manage API versioning?**  
A: URL versioning (`/api/v1`) or header-based versioning.

---

# 🧪 Testing — Q & A

**Q: How do you test Flask apps?**  
A: Using pytest, test clients, and isolated databases.

**Q: How do you test React apps?**  
A: Using Jest and React Testing Library.

**Q: Unit vs integration tests?**  
A: Unit tests isolate components; integration tests verify real interactions.

**Q: How do you mock API calls in React?**  
A: Using mock servers, Jest mocks, or MSW.

---

# 🚀 Deployment & Production — Q & A

**Q: How do you deploy Flask?**  
A: WSGI server (Gunicorn), reverse proxy (Nginx), containerization.

**Q: How do you deploy React?**  
A: Build static assets and serve via CDN or web server.

**Q: How do you handle CI/CD?**  
A: Automated tests, linting, build pipelines, and deployment workflows.

**Q: How do you handle secrets in production?**  
A: Environment variables and secret managers — never in code.

---

# ⚡ Strong-Signal Questions (Senior Level)

**Q: How do you prevent over-fetching in React?**  
A: Memoization, pagination, selective API endpoints, or GraphQL.

**Q: How do you prevent N+1 queries in Flask APIs?**  
A: Proper joins, eager loading, and query optimization.

**Q: How do you ensure frontend-backend contract stability?**  
A: API schemas, OpenAPI specs, and contract tests.

**Q: How do you optimize full-stack performance?**  
A: Caching, minimizing network calls, compression, and code splitting.