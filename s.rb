# Violation of the Single Responsibility Principle in Ruby
class Order
  def initialize(line_items, tax, account)
    @account = account
    @tax = tax
    @subtotal = line_items.sum(:price)
    @receipt = nil
  end

  def generate_receipt
    @receipt = @line_items.map do |item|
      "#{item.description}............$ #{item.price}"
    end
    @receipt.push("SUBTOTAL.........$ #{@subtotal}")
    @receipt.push("TAX..............$ #{@tax}")
    @receipt.push("--------------------------------------")
    @receipt.push("TOTAL............$ #{@subtotal + @tax}")
    return @receipt.join("\n")
  end

  def send_receipt
    EmailSystem.deliver(
      from: 'orders@example.com',
      to: @account.email,
      subject: 'Your Order Receipt',
      body: @receipt
    )
  end
end

order = Order.new(line_items, account)
order.generate_receipt
order.send_receipt

#####
o = Order.new(line_items, account)
print(o.generate_receipt)
