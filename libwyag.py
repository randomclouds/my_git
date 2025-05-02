import argparse, configparser
import grp, pwd, os, re, sys, zlib
import hashlib
from datetime import datetime
from fnmatch import fnmatch
from math import ceil


#I think it's used to create a object for parse
argparser = argparse.ArgumentParser(description="The stupidest content tracker")

argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True #It means we need completed innovation

def main(argv=sys.argv[1:]): #receive the CLI argument
    args = argparser.parse_args(argv) #specify all arguments
    match args.command: #match diff sub_command
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "commit"       : cmd_commit(args)
        case "hash_object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        case "log"          : cmd_log(args)
        case "ls-files"     : cmd_ls_files(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_res(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              : print("Bad command.")