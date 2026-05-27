from src.same_tree import TreeNode, is_same_tree


def test_example_1_identical_trees():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) is True


def test_example_2_different_structure():
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) is False


def test_example_3_different_values():
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p, q) is False


def test_both_empty():
    assert is_same_tree(None, None) is True


def test_one_empty_one_not():
    assert is_same_tree(None, TreeNode(1)) is False
    assert is_same_tree(TreeNode(1), None) is False


def test_single_node_same_value():
    assert is_same_tree(TreeNode(42), TreeNode(42)) is True


def test_single_node_different_value():
    assert is_same_tree(TreeNode(1), TreeNode(2)) is False


def test_deeper_tree_identical():
    p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert is_same_tree(p, q) is True


def test_deeper_tree_one_node_differs():
    p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3))
    assert is_same_tree(p, q) is False


def test_negative_values():
    p = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    q = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    assert is_same_tree(p, q) is True
