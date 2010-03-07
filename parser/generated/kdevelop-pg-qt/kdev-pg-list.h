/*
  This file is part of kdev-pg
  Copyright 2005, 2006 Roberto Raggi <roberto@kdevelop.org>

  Permission to use, copy, modify, distribute, and sell this software and its
  documentation for any purpose is hereby granted without fee, provided that
  the above copyright notice appear in all copies and that both that
  copyright notice and this permission notice appear in supporting
  documentation.

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
  KDEVELOP TEAM BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
  AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

//krazy:exclude-all=inline
#ifndef KDEV_PG_LIST_H
#define KDEV_PG_LIST_H

#include "kdev-pg-memory-pool.h"

namespace KDevPG
{

template <typename _Tp>
struct ListNode
{
  _Tp element;
  int index;
  mutable const ListNode<_Tp> *next;

  static ListNode *create(const _Tp &element, MemoryPool *p)
  {
    ListNode<_Tp> *node = new (p->allocate(sizeof(ListNode))) ListNode();
    node->element = element;
    node->index = 0;
    node->next = node;

    return node;
  }

  static ListNode *create(const ListNode *n1, const _Tp &element, MemoryPool *p)
  {
    ListNode<_Tp> *n2 = ListNode::create(element, p);

    n2->index = n1->index + 1;
    n2->next = n1->next;
    n1->next = n2;

    return n2;
  }

  inline const ListNode<_Tp> *at(int index) const
  {
    const ListNode<_Tp> *node = this;
    while (index != node->index)
      node = node->next;

    return node;
  }

  inline bool hasNext() const
  { return index < next->index; }

  inline int count() const
  { return 1 + back()->index; }

  inline const ListNode<_Tp> *front() const
  { return back()->next; }

  inline const ListNode<_Tp> *back() const
  {
    const ListNode<_Tp> *node = this;
    while (node->hasNext())
      node = node->next;

    return node;
  }
};

template <class _Tp>
inline const ListNode<_Tp> *snoc(const ListNode<_Tp> *list,
                                  const _Tp &element, MemoryPool *p)
{
  if (!list)
    return ListNode<_Tp>::create(element, p);

  return ListNode<_Tp>::create(list->back(), element, p);
}

}

#endif // KDEV_PG_LIST_H


