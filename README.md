# 🐍 Python Interview — Q & A

### Q: What's the difference between a list and a tuple?
**A:** Lists are mutable, tuples are immutable. Tuples are faster, hashable, and safer for fixed data.

### Q: How does Python handle memory management?
**A:** Through reference counting and a cyclic garbage collector for circular references.

### Q: What are mutable vs immutable types?
**A:** Mutable types can change in place (list, dict, set). Immutable types create new objects when modified (int, str, tuple).

### Q: What are `*args` and `**kwargs`?
**A:** `*args` captures extra positional arguments as a tuple; `**kwargs` captures keyword arguments as a dict.

### Q: What is the GIL?
**A:** The Global Interpreter Lock ensures only one thread executes Python bytecode at a time, simplifying memory safety.

### Q: When should you use multithreading vs multiprocessing in Python?
**A:** Threads for I/O-bound tasks; multiprocessing for CPU-bound tasks to bypass the GIL.

### Q: What is a decorator?
**A:** A function that wraps another function to extend behavior without modifying its code.

### Q: Difference between `__str__` and `__repr__`? 
**A:** `__str__` is user-facing; `__repr__` is developer-facing and unambiguous.

### Q: What are comprehensions?
**A:** A concise syntax for constructing collections, often faster and more readable than loops.

### Q: What happens with `a = b = []`?
**A:** Both variables reference the same list; mutations affect both.

---

### Q: Difference between shallow and deep copy?
**A:** Shallow copies references; deep copies recursively copy all nested objects.

### Q: Generators vs iterators?
**A:** Generators use yield and produce values lazily; iterators implement `__next__`.

### Q: What is a context manager?
**A:** An object that manages setup and teardown via `__enter__` and `__exit__`.

### Q: How does asyncio work?
**A:** It uses an event loop to run coroutines cooperatively in a single thread.

### Q: What is monkey patching?
**A:** Modifying code at runtime; powerful but risky.

### Q: What is MRO?
**A:** Method Resolution Order — the order Python follows to resolve inherited methods.

---

# 🧮 SQL Interview — Q & A

### Q: Difference between WHERE and HAVING?
**A:** WHERE filters rows before aggregation; HAVING filters after aggregation.

### Q: Primary key vs foreign key?
**A:** A primary key uniquely identifies a row; a foreign key references another table's primary key.

### Q: Explain SQL joins.
**A:** INNER returns matches; LEFT/RIGHT return all rows from one side; FULL returns all rows.

### Q: What is normalization?
**A:** Structuring data to reduce redundancy and improve integrity.

### Q: When would you denormalize?
**A:** For read-heavy systems where performance outweighs strict normalization.

### Q: DELETE vs TRUNCATE vs DROP?
**A:** DELETE removes rows, TRUNCATE removes all rows fast, DROP removes the table.

### Q: What is an index?
**A:** A data structure that speeds up reads at the cost of write performance and storage.

---

### Q: What are window functions?
**A:** Functions that compute values across related rows without collapsing them.

### Q: What is an execution plan?
**A:** The database's strategy for executing a query.

### Q: Explain ACID.
**A:** Atomicity, Consistency, Isolation, Durability — guarantees for transactions.

### Q: What is a transaction?
**A:** A group of operations that either fully succeed or fully fail.

### Q: OLTP vs OLAP?
**A:** OLTP handles frequent small transactions; OLAP handles large analytical queries.

---

# 🌐 JavaScript Interview — Q & A

### Q: Difference between var, let, and const?
**A:** var is function-scoped; let and const are block-scoped; const prevents reassignment.

### Q: What is hoisting?
**A:** Declarations are moved to the top of their scope during compilation.

### Q: What is a closure?
**A:** A function that retains access to its outer scope after execution.

### Q: Explain this.
**A:** Its value depends on how a function is called; arrow functions inherit it.

### Q: == vs ===?
**A:** == allows coercion; === enforces strict equality.

### Q: What is event bubbling vs capturing?
**A:** Bubbling moves events up the DOM; capturing moves down.

### Q: What is a promise?
**A:** An object representing a future value with pending, fulfilled, or rejected states.

### Q: What does async/await do?
**A:** Provides synchronous-looking syntax over promises.

---

### Q: How does the event loop work?
**A:** It processes the call stack, then microtasks, then macrotasks.

### Q: What is prototypal inheritance?
**A:** Objects inherit properties from other objects via a prototype chain.

### Q: Debounce vs throttle?
**A:** Debounce delays execution; throttle limits execution frequency.

### Q: How does JS manage memory?
**A:** Automatic garbage collection; leaks come from lingering references.

### Q: bind, call, and apply?
**A:** All set this; bind returns a new function, call/apply invoke immediately.

---

# 🧠 General Programming — Q & A

### Q: When use arrays vs linked lists?
**A:** Arrays for fast access; linked lists for fast inserts/deletes.

### Q: Stack vs queue?
**A:** Stack is LIFO; queue is FIFO.

### Q: How does a hash table work?
**A:** A hash function maps keys to buckets; collisions are resolved internally.

### Q: BFS vs DFS?
**A:** BFS explores level by level; DFS explores depth-first.

### Q: What is Big-O?
**A:** A measure of algorithmic scalability.

### Q: Quicksort vs mergesort?
**A:** Quicksort is in-place and cache-friendly; mergesort is stable and predictable.

### Q: Greedy vs dynamic programming?
**A:** Greedy makes local choices; DP solves overlapping subproblems optimally.

### Q: How do you detect a cycle in a graph?
**A:** Use a visited set or Floyd's cycle detection algorithm.

---

# 🧱 System Design — Q & A

### Q: What is REST?
**A:** A stateless, resource-oriented architecture using HTTP verbs.

### Q: REST vs GraphQL?
**A:** REST has fixed endpoints; GraphQL allows flexible queries.

### Q: What is idempotency?
**A:** Multiple identical requests yield the same result.

### Q: What is eventual consistency?
**A:** Data becomes consistent over time.

### Q: What is a race condition?
**A:** Multiple actors access shared state unsafely.

### Q: What is a deadlock?
**A:** Circular waiting for resources.

### Q: How would you design a rate limiter?
**A:** Token bucket or sliding window, often Redis-backed.

### Q: How would you design a URL shortener?
**A:** Unique ID generation, persistent storage, caching, and redirects.

---

# 🧪 Practical / Behavioral — Q & A

### Q: How do you debug a production issue?
**A:** Reproduce, inspect logs/metrics, isolate, fix, and write a postmortem.

### Q: How do you approach legacy code?
**A:** Add tests first, then refactor incrementally.

### Q: What makes code testable?
**A:** Small functions, clear boundaries, dependency injection.

### Q: Unit vs integration tests?
**A:** Unit tests isolate logic; integration tests verify components together.

### Q: How do you review code?
**A:** Focus on correctness, clarity, maintainability, and edge cases.

---

# ⚡ Strong-Signal Questions — Q & A

### Q: Describe a system you built.
**A:** Focus on tradeoffs, constraints, and lessons learned.

### Q: A technical decision you regret?
**A:** Own the mistake and explain what you learned.

### Q: Performance vs readability?
**A:** Default to readability; optimize proven bottlenecks.

### Q: When do you refactor?
**A:** When change cost becomes high or complexity increases.
