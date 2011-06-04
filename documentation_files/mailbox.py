#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
""":synopsis: Manipulate mailboxes in various formats
"""
class Mailbox:


	"""
	A mailbox, which may be inspected and modified.
	
	The :class:`Mailbox` class defines an interface and is not intended to be
	instantiated.  Instead, format-specific subclasses should inherit from
	:class:`Mailbox` and your code should instantiate a particular subclass.
	
	The :class:`Mailbox` interface is dictionary-like, with small keys
	corresponding to messages. Keys are issued by the :class:`Mailbox` instance
	with which they will be used and are only meaningful to that :class:`Mailbox`
	instance. A key continues to identify a message even if the corresponding
	message is modified, such as by replacing it with another message.
	
	Messages may be added to a :class:`Mailbox` instance using the set-like
	method :meth:`add` and removed using a ``del`` statement or the set-like
	methods :meth:`remove` and :meth:`discard`.
	
	:class:`Mailbox` interface semantics differ from dictionary semantics in some
	noteworthy ways. Each time a message is requested, a new representation
	(typically a :class:`Message` instance) is generated based upon the current
	state of the mailbox. Similarly, when a message is added to a
	:class:`Mailbox` instance, the provided message representation's contents are
	copied. In neither case is a reference to the message representation kept by
	the :class:`Mailbox` instance.
	
	The default :class:`Mailbox` iterator iterates over message representations,
	not keys as the default dictionary iterator does. Moreover, modification of a
	mailbox during iteration is safe and well-defined. Messages added to the
	mailbox after an iterator is created will not be seen by the
	iterator. Messages removed from the mailbox before the iterator yields them
	will be silently skipped, though using a key from an iterator may result in a
	:exc:`KeyError` exception if the corresponding message is subsequently
	removed.
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class Maildir:


	"""
	A subclass of :class:`Mailbox` for mailboxes in Maildir format. Parameter
	*factory* is a callable object that accepts a file-like message representation
	(which behaves as if opened in binary mode) and returns a custom representation.
	If *factory* is ``None``, :class:`MaildirMessage` is used as the default message
	representation. If *create* is ``True``, the mailbox is created if it does not
	exist.
	
	It is for historical reasons that *factory* defaults to :class:`rfc822.Message`
	and that *dirname* is named as such rather than *path*. For a :class:`Maildir`
	instance that behaves like instances of other :class:`Mailbox` subclasses, set
	*factory* to ``None``.
	
	Maildir is a directory-based mailbox format invented for the qmail mail
	transfer agent and now widely supported by other programs. Messages in a
	Maildir mailbox are stored in separate files within a common directory
	structure. This design allows Maildir mailboxes to be accessed and modified
	by multiple unrelated programs without data corruption, so file locking is
	unnecessary.
	
	Maildir mailboxes contain three subdirectories, namely: :file:`tmp`,
	:file:`new`, and :file:`cur`. Messages are created momentarily in the
	:file:`tmp` subdirectory and then moved to the :file:`new` subdirectory to
	finalize delivery. A mail user agent may subsequently move the message to the
	:file:`cur` subdirectory and store information about the state of the message
	in a special "info" section appended to its file name.
	
	Folders of the style introduced by the Courier mail transfer agent are also
	supported. Any subdirectory of the main mailbox is considered a folder if
	``'.'`` is the first character in its name. Folder names are represented by
	:class:`Maildir` without the leading ``'.'``. Each folder is itself a Maildir
	mailbox but should not contain other folders. Instead, a logical nesting is
	indicated using ``'.'`` to delimit levels, e.g., "Archived.2005.07".
	
	"""
	
	
	def __init__(self, dirname,factory=rfc822):
		pass
	
	


class mbox:


	"""
	A subclass of :class:`Mailbox` for mailboxes in mbox format. Parameter *factory*
	is a callable object that accepts a file-like message representation (which
	behaves as if opened in binary mode) and returns a custom representation. If
	*factory* is ``None``, :class:`mboxMessage` is used as the default message
	representation. If *create* is ``True``, the mailbox is created if it does not
	exist.
	
	The mbox format is the classic format for storing mail on Unix systems. All
	messages in an mbox mailbox are stored in a single file with the beginning of
	each message indicated by a line whose first five characters are "From ".
	
	Several variations of the mbox format exist to address perceived shortcomings in
	the original. In the interest of compatibility, :class:`mbox` implements the
	original format, which is sometimes referred to as :dfn:`mboxo`. This means that
	the :mailheader:`Content-Length` header, if present, is ignored and that any
	occurrences of "From " at the beginning of a line in a message body are
	transformed to ">From " when storing the message, although occurrences of ">From
	" are not transformed to "From " when reading the message.
	
	Some :class:`Mailbox` methods implemented by :class:`mbox` deserve special
	remarks:
	
	
	"""
	
	
	def __init__(self, path,factory=None,create=True):
		pass
	
	


class MH:


	"""
	A subclass of :class:`Mailbox` for mailboxes in MH format. Parameter *factory*
	is a callable object that accepts a file-like message representation (which
	behaves as if opened in binary mode) and returns a custom representation. If
	*factory* is ``None``, :class:`MHMessage` is used as the default message
	representation. If *create* is ``True``, the mailbox is created if it does not
	exist.
	
	MH is a directory-based mailbox format invented for the MH Message Handling
	System, a mail user agent. Each message in an MH mailbox resides in its own
	file. An MH mailbox may contain other MH mailboxes (called :dfn:`folders`) in
	addition to messages. Folders may be nested indefinitely. MH mailboxes also
	support :dfn:`sequences`, which are named lists used to logically group
	messages without moving them to sub-folders. Sequences are defined in a file
	called :file:`.mh_sequences` in each folder.
	
	The :class:`MH` class manipulates MH mailboxes, but it does not attempt to
	emulate all of :program:`mh`'s behaviors. In particular, it does not modify
	and is not affected by the :file:`context` or :file:`.mh_profile` files that
	are used by :program:`mh` to store its state and configuration.
	
	:class:`MH` instances have all of the methods of :class:`Mailbox` in addition
	to the following:
	
	
	"""
	
	
	def __init__(self, path,factory=None,create=True):
		pass
	
	


class Babyl:


	"""
	A subclass of :class:`Mailbox` for mailboxes in Babyl format. Parameter
	*factory* is a callable object that accepts a file-like message representation
	(which behaves as if opened in binary mode) and returns a custom representation.
	If *factory* is ``None``, :class:`BabylMessage` is used as the default message
	representation. If *create* is ``True``, the mailbox is created if it does not
	exist.
	
	Babyl is a single-file mailbox format used by the Rmail mail user agent
	included with Emacs. The beginning of a message is indicated by a line
	containing the two characters Control-Underscore (``'\037'``) and Control-L
	(``'\014'``). The end of a message is indicated by the start of the next
	message or, in the case of the last message, a line containing a
	Control-Underscore (``'\037'``) character.
	
	Messages in a Babyl mailbox have two sets of headers, original headers and
	so-called visible headers. Visible headers are typically a subset of the
	original headers that have been reformatted or abridged to be more
	attractive. Each message in a Babyl mailbox also has an accompanying list of
	:dfn:`labels`, or short strings that record extra information about the
	message, and a list of all user-defined labels found in the mailbox is kept
	in the Babyl options section.
	
	:class:`Babyl` instances have all of the methods of :class:`Mailbox` in
	addition to the following:
	
	
	"""
	
	
	def __init__(self, path,factory=None,create=True):
		pass
	
	


class MMDF:


	"""
	A subclass of :class:`Mailbox` for mailboxes in MMDF format. Parameter *factory*
	is a callable object that accepts a file-like message representation (which
	behaves as if opened in binary mode) and returns a custom representation. If
	*factory* is ``None``, :class:`MMDFMessage` is used as the default message
	representation. If *create* is ``True``, the mailbox is created if it does not
	exist.
	
	MMDF is a single-file mailbox format invented for the Multichannel Memorandum
	Distribution Facility, a mail transfer agent. Each message is in the same
	form as an mbox message but is bracketed before and after by lines containing
	four Control-A (``'\001'``) characters. As with the mbox format, the
	beginning of each message is indicated by a line whose first five characters
	are "From ", but additional occurrences of "From " are not transformed to
	">From " when storing messages because the extra message separator lines
	prevent mistaking such occurrences for the starts of subsequent messages.
	
	Some :class:`Mailbox` methods implemented by :class:`MMDF` deserve special
	remarks:
	
	
	"""
	
	
	def __init__(self, path,factory=None,create=True):
		pass
	
	


class Message:


	"""
	A subclass of the :mod:`email.Message` module's :class:`Message`. Subclasses of
	:class:`mailbox.Message` add mailbox-format-specific state and behavior.
	
	If *message* is omitted, the new instance is created in a default, empty state.
	If *message* is an :class:`email.Message.Message` instance, its contents are
	copied; furthermore, any format-specific information is converted insofar as
	possible if *message* is a :class:`Message` instance. If *message* is a string
	or a file, it should contain an :rfc:`2822`\ -compliant message, which is read
	and parsed.
	
	The format-specific state and behaviors offered by subclasses vary, but in
	general it is only the properties that are not specific to a particular
	mailbox that are supported (although presumably the properties are specific
	to a particular mailbox format). For example, file offsets for single-file
	mailbox formats and file names for directory-based mailbox formats are not
	retained, because they are only applicable to the original mailbox. But state
	such as whether a message has been read by the user or marked as important is
	retained, because it applies to the message itself.
	
	There is no requirement that :class:`Message` instances be used to represent
	messages retrieved using :class:`Mailbox` instances. In some situations, the
	time and memory required to generate :class:`Message` representations might
	not not acceptable. For such situations, :class:`Mailbox` instances also
	offer string and file-like representations, and a custom message factory may
	be specified when a :class:`Mailbox` instance is initialized.
	
	
	.. class:`MaildirMessage`
	^^^^^^^^^^^^^^^^^^^^^^^
	
	
	"""
	
	
	def __init__(self, message):
		pass
	
	


class MaildirMessage:


	"""
	A message with Maildir-specific behaviors. Parameter *message* has the same
	meaning as with the :class:`Message` constructor.
	
	Typically, a mail user agent application moves all of the messages in the
	:file:`new` subdirectory to the :file:`cur` subdirectory after the first time
	the user opens and closes the mailbox, recording that the messages are old
	whether or not they've actually been read. Each message in :file:`cur` has an
	"info" section added to its file name to store information about its state.
	(Some mail readers may also add an "info" section to messages in
	:file:`new`.)  The "info" section may take one of two forms: it may contain
	"2," followed by a list of standardized flags (e.g., "2,FR") or it may
	contain "1," followed by so-called experimental information. Standard flags
	for Maildir messages are as follows:
	
	+------+---------+--------------------------------+
	| Flag | Meaning | Explanation                    |
	+======+=========+================================+
	| D    | Draft   | Under composition              |
	+------+---------+--------------------------------+
	| F    | Flagged | Marked as important            |
	+------+---------+--------------------------------+
	| P    | Passed  | Forwarded, resent, or bounced  |
	+------+---------+--------------------------------+
	| R    | Replied | Replied to                     |
	+------+---------+--------------------------------+
	| S    | Seen    | Read                           |
	+------+---------+--------------------------------+
	| T    | Trashed | Marked for subsequent deletion |
	+------+---------+--------------------------------+
	
	:class:`MaildirMessage` instances offer the following methods:
	
	
	"""
	
	
	def __init__(self, message):
		pass
	
	


class mboxMessage:


	"""
	A message with mbox-specific behaviors. Parameter *message* has the same meaning
	as with the :class:`Message` constructor.
	
	Messages in an mbox mailbox are stored together in a single file. The
	sender's envelope address and the time of delivery are typically stored in a
	line beginning with "From " that is used to indicate the start of a message,
	though there is considerable variation in the exact format of this data among
	mbox implementations. Flags that indicate the state of the message, such as
	whether it has been read or marked as important, are typically stored in
	:mailheader:`Status` and :mailheader:`X-Status` headers.
	
	Conventional flags for mbox messages are as follows:
	
	+------+----------+--------------------------------+
	| Flag | Meaning  | Explanation                    |
	+======+==========+================================+
	| R    | Read     | Read                           |
	+------+----------+--------------------------------+
	| O    | Old      | Previously detected by MUA     |
	+------+----------+--------------------------------+
	| D    | Deleted  | Marked for subsequent deletion |
	+------+----------+--------------------------------+
	| F    | Flagged  | Marked as important            |
	+------+----------+--------------------------------+
	| A    | Answered | Replied to                     |
	+------+----------+--------------------------------+
	
	The "R" and "O" flags are stored in the :mailheader:`Status` header, and the
	"D", "F", and "A" flags are stored in the :mailheader:`X-Status` header. The
	flags and headers typically appear in the order mentioned.
	
	:class:`mboxMessage` instances offer the following methods:
	
	
	"""
	
	
	def __init__(self, message):
		pass
	
	


class MHMessage:


	"""
	A message with MH-specific behaviors. Parameter *message* has the same meaning
	as with the :class:`Message` constructor.
	
	MH messages do not support marks or flags in the traditional sense, but they
	do support sequences, which are logical groupings of arbitrary messages. Some
	mail reading programs (although not the standard :program:`mh` and
	:program:`nmh`) use sequences in much the same way flags are used with other
	formats, as follows:
	
	+----------+------------------------------------------+
	| Sequence | Explanation                              |
	+==========+==========================================+
	| unseen   | Not read, but previously detected by MUA |
	+----------+------------------------------------------+
	| replied  | Replied to                               |
	+----------+------------------------------------------+
	| flagged  | Marked as important                      |
	+----------+------------------------------------------+
	
	:class:`MHMessage` instances offer the following methods:
	
	
	"""
	
	
	def __init__(self, message):
		pass
	
	


class BabylMessage:


	"""
	A message with Babyl-specific behaviors. Parameter *message* has the same
	meaning as with the :class:`Message` constructor.
	
	Certain message labels, called :dfn:`attributes`, are defined by convention
	to have special meanings. The attributes are as follows:
	
	+-----------+------------------------------------------+
	| Label     | Explanation                              |
	+===========+==========================================+
	| unseen    | Not read, but previously detected by MUA |
	+-----------+------------------------------------------+
	| deleted   | Marked for subsequent deletion           |
	+-----------+------------------------------------------+
	| filed     | Copied to another file or mailbox        |
	+-----------+------------------------------------------+
	| answered  | Replied to                               |
	+-----------+------------------------------------------+
	| forwarded | Forwarded                                |
	+-----------+------------------------------------------+
	| edited    | Modified by the user                     |
	+-----------+------------------------------------------+
	| resent    | Resent                                   |
	+-----------+------------------------------------------+
	
	By default, Rmail displays only visible headers. The :class:`BabylMessage`
	class, though, uses the original headers because they are more
	complete. Visible headers may be accessed explicitly if desired.
	
	:class:`BabylMessage` instances offer the following methods:
	
	
	"""
	
	
	def __init__(self, message):
		pass
	
	


class MMDFMessage:


	"""
	A message with MMDF-specific behaviors. Parameter *message* has the same meaning
	as with the :class:`Message` constructor.
	
	As with message in an mbox mailbox, MMDF messages are stored with the
	sender's address and the delivery date in an initial line beginning with
	"From ".  Likewise, flags that indicate the state of the message are
	typically stored in :mailheader:`Status` and :mailheader:`X-Status` headers.
	
	Conventional flags for MMDF messages are identical to those of mbox message
	and are as follows:
	
	+------+----------+--------------------------------+
	| Flag | Meaning  | Explanation                    |
	+======+==========+================================+
	| R    | Read     | Read                           |
	+------+----------+--------------------------------+
	| O    | Old      | Previously detected by MUA     |
	+------+----------+--------------------------------+
	| D    | Deleted  | Marked for subsequent deletion |
	+------+----------+--------------------------------+
	| F    | Flagged  | Marked as important            |
	+------+----------+--------------------------------+
	| A    | Answered | Replied to                     |
	+------+----------+--------------------------------+
	
	The "R" and "O" flags are stored in the :mailheader:`Status` header, and the
	"D", "F", and "A" flags are stored in the :mailheader:`X-Status` header. The
	flags and headers typically appear in the order mentioned.
	
	:class:`MMDFMessage` instances offer the following methods, which are
	identical to those offered by :class:`mboxMessage`:
	
	
	"""
	
	
	def __init__(self, message):
		pass
	
	


class UnixMailbox:


	"""
	Access to a classic Unix-style mailbox, where all messages are contained in a
	single file and separated by ``From`` (a.k.a. ``From_``) lines.  The file object
	*fp* points to the mailbox file.  The optional *factory* parameter is a callable
	that should create new message objects.  *factory* is called with one argument,
	*fp* by the :meth:`!next` method of the mailbox object.  The default is the
	:class:`rfc822.Message` class (see the :mod:`rfc822` module -- and the note
	below).
	
	"""
	
	
	def __init__(self, fp,factory):
		pass
	
	


class PortableUnixMailbox:


	"""
	A less-strict version of :class:`UnixMailbox`, which considers only the ``From``
	at the beginning of the line separating messages.  The "*name* *time*" portion
	of the From line is ignored, to protect against some variations that are
	observed in practice.  This works since lines in the message which begin with
	``'From '`` are quoted by mail handling software at delivery-time.
	
	
	"""
	
	
	def __init__(self, fp,factory):
		pass
	
	


class MmdfMailbox:


	"""
	Access an MMDF-style mailbox, where all messages are contained in a single file
	and separated by lines consisting of 4 control-A characters.  The file object
	*fp* points to the mailbox file. Optional *factory* is as with the
	:class:`UnixMailbox` class.
	
	
	"""
	
	
	def __init__(self, fp,factory):
		pass
	
	


class MHMailbox:


	"""
	Access an MH mailbox, a directory with each message in a separate file with a
	numeric name. The name of the mailbox directory is passed in *dirname*.
	*factory* is as with the :class:`UnixMailbox` class.
	
	
	"""
	
	
	def __init__(self, dirname,factory):
		pass
	
	


