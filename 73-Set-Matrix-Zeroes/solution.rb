def set_zeroes(matrix)
  return if matrix.empty?
  m = matrix.size
  n = matrix[0].size
  row0maker = (0...n).any? { |j| matrix[0][j].zero? }
  col0maker = (0...m).any? { |i| matrix[i][0].zero? }

  (1...m).each do |i|
    (1...n).each do |j|
      if matrix[i][j].zero?
        matrix[0][j] = matrix[i][0] = 0
      end
    end
  end

  (1...m).each do |i|
    (1...n).each do |j|
      if matrix[0][j].zero? || matrix[i][0].zero?
        matrix[i][j] = 0
      end
    end
  end

  (0...n).each { |j| matrix[0][j] = 0 } if row0maker
  (0...m).each { |i| matrix[i][0] = 0 } if col0maker


end