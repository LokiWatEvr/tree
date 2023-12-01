import turtle
def draw_tree(branch_len, t ):
    if branch_len < 5:
        return
    else:
       t.forward(branch_len)
       t.right(20)
       draw_tree(branch_len - 15, t)
       t.left(40)
       draw_tree(branch_len - 15, t)
       t.right(20)
       t.backward(branch_len)

tree = turtle.Turtle()

tree.left(90)
tree.up()
tree.backward(200)
tree.down()
tree.color("brown")
tree.speed(10)
draw_tree(100,tree)
turtle.done