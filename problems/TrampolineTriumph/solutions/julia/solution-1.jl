g(f) = x -> (6 - 2 * f * sin(x / 2) - 2 * f * sin(x / 5) - 2 * f * sin(x / 7)) * (.9 + ((1 + sin((x * f) / 3)) / 20))

function maximize(g, range)
  for delta in [1e-6, 1e-7, 1e-8, 1e-9, 1e-10]
    range = range[1]:delta:range[end]
    while length(range) >= 10
      mid = div(length(range), 2)
      range = if g(range[mid]) < g(range[mid+1])
        range[mid+1:end]
      else
        range[1:mid]
      end
    end
  end
  maximum(g, range)
end

readline()
players = map(f -> g(parse(Float64, f)), split(readline()))
scores = zeros(Int, size(players))

m = parse(Int, readline())
for i in 1:m
  milestone = map(x -> parse(Float64, x), split(readline()))
  heights = map(g -> maximize(g, milestone), players)
  winner = findmax(heights)[2]
  scores[winner] += 1
end

for (p, s) in sort(collect(enumerate(scores)), by=x->x[2], rev=true)
  println(p, " ", s)
end