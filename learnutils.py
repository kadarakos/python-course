from os import getcwd, listdir
from os.path import isdir
from os.path import join as pjoin

ALONG = u'\u2500'
DOWN = u'\u2502'
DOWN_RIGHT = u'\u251c'
ELBOW_RIGHT = u'\u2514'
BLUE = u'\033[94m'
ENDC = u'\033[0m'
DOWN_RIGHT_ALONG = DOWN_RIGHT + ALONG * 2 + u" "
ELBOW_RIGHT_ALONG = ELBOW_RIGHT + ALONG * 2 + u" "
CONTINUE_INDENT = DOWN + u' ' * 3
FINISH_INDENT = u' ' * 4

def print_path(root_path, path, indent_str, last_entry=False):
    """ Print individual `path` (file or directory name) from `root_path`

    Parameters
    ----------
    root_path : str
        path containing `path`
    path : str
        file name or directory name
    indent_str : str
        string to prefix to entry for this `path`
    last_entry : bool, optional
        Whether this is the last entry in a list of paths.

    Returns
    -------
    None
    """
    full_path = pjoin(root_path, path)
    have_dir = isdir(full_path)
    leader = ELBOW_RIGHT_ALONG if last_entry else DOWN_RIGHT_ALONG
    path_colored = BLUE + path + ENDC if have_dir else path
    print(indent_str + leader + path_colored)
    if have_dir:
        new_indent = FINISH_INDENT if last_entry else CONTINUE_INDENT
        print_tree(full_path, indent_str + new_indent)

def print_tree(root_path=None, indent_str=u''):
    """ Print tree structure starting from `root_path`

    Parameters
    ----------
    root_path : None or str, optional
        path from which to print directory tree structure.  If None, use current
        directory.
    indent_str : str, optional
        prefix to print for every entry in the tree.  Usually '', and then set
        by recursion into the function when printing subdirectories.

    Returns
    -------
    None
    """
    if root_path is None:
        root_path = getcwd()
    # ensure return of unicode paths from listdir
    root_path = unicode(root_path)
    paths = sorted(listdir(root_path))
    if len(paths) == 0:
        return
    for path in paths[:-1]:
        if path != '.git' and path != '.ipynb_checkpoints':
            print_path(root_path, path, indent_str, False)
    #if root_path != '.git':
    print_path(root_path, paths[-1], indent_str, True)
