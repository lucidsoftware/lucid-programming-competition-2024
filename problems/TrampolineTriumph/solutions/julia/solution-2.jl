g(f, x) = (6 - 2f * sin(x / 2) - 2f * sin(x / 5) - 2f * sin(x / 7)) * (.9 + ((1 + sin((x * f) / 3)) / 20))

function maximize(f, range)
  l, r = range
  while r - l > 1e-9
    mid = (l + r) / 2
    if g(f, mid) < g(f, mid + 1e-9)
      l = mid
    else
      r = mid
    end
  end
  g(f, l)
end

readline()
players = map(f -> parse(Float64, f), split(readline()))
scores = zeros(Int, size(players))

m = parse(Int, readline())
for i in 1:m
  milestone = map(x -> parse(Float64, x), split(readline()))
  heights = map(f -> maximize(f, milestone), players)
  winner = findmax(heights)
  scores[winner[2]] += 1
end

for (p, s) in sort(collect(enumerate(scores)), by=x->x[2], rev=true)
  println(p, " ", s)
end