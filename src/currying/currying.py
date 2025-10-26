def curry(func, n):
    assert n >= 0, "Error: n can't be negative"
    assert isinstance(n, int), "Error: n should be natural number"
    if n == 0:
            return func
    else:
        def start(arg):
            args = [arg]
            if n == 1:
                return func(arg)
            def continuation(arg):
                args.append(arg)
                if len(args) == n:
                    return func(*args)
                return continuation
            
            return continuation
    
        return start

def uncurry(curried_func, n):
    assert n >= 0, "Error: n can't be negative"
    assert isinstance(n, int), "Error: n should be natural number"

    if n == 0:
        return curried_func
    else:
        def uncurried(*args):
            assert len(args) == n, f"Error: {n} arguments expected, {len(args)} given"
            if n == 1:
                return curried_func(args[0]) 
            result = curried_func
            for arg in args:
                result = result(arg)
            return result
    
    return uncurried
