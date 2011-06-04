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
	
	def add(self, message):
		"""
		Add *message* to the mailbox and return the key that has been assigned to
		it.
		
		Parameter *message* may be a :class:`Message` instance, an
		:class:`email.Message.Message` instance, a string, or a file-like object
		(which should be open in text mode). If *message* is an instance of the
		appropriate format-specific :class:`Message` subclass (e.g., if it's an
		:class:`mboxMessage` instance and this is an :class:`mbox` instance), its
		format-specific information is used. Otherwise, reasonable defaults for
		format-specific information are used.
		
		
		"""
		pass
		
	def remove(self, key):
		"""__delitem__(key)
		discard(key)
		
		Delete the message corresponding to *key* from the mailbox.
		
		If no such message exists, a :exc:`KeyError` exception is raised if the
		method was called as :meth:`remove` or :meth:`__delitem__` but no
		exception is raised if the method was called as :meth:`discard`. The
		behavior of :meth:`discard` may be preferred if the underlying mailbox
		format supports concurrent modification by other processes.
		
		
		"""
		pass
		
	def __setitem__(self, key,message):
		"""
		Replace the message corresponding to *key* with *message*. Raise a
		:exc:`KeyError` exception if no message already corresponds to *key*.
		
		As with :meth:`add`, parameter *message* may be a :class:`Message`
		instance, an :class:`email.Message.Message` instance, a string, or a
		file-like object (which should be open in text mode). If *message* is an
		instance of the appropriate format-specific :class:`Message` subclass
		(e.g., if it's an :class:`mboxMessage` instance and this is an
		:class:`mbox` instance), its format-specific information is
		used. Otherwise, the format-specific information of the message that
		currently corresponds to *key* is left unchanged.
		
		
		"""
		pass
		
	def iterkeys(self, ):
		"""keys()
		
		Return an iterator over all keys if called as :meth:`iterkeys` or return a
		list of keys if called as :meth:`keys`.
		
		
		"""
		pass
		
	def itervalues(self, ):
		"""__iter__()
		values()
		
		Return an iterator over representations of all messages if called as
		:meth:`itervalues` or :meth:`__iter__` or return a list of such
		representations if called as :meth:`values`. The messages are represented
		as instances of the appropriate format-specific :class:`Message` subclass
		unless a custom message factory was specified when the :class:`Mailbox`
		instance was initialized.
		
		"""
		pass
		
	def iteritems(self, ):
		"""items()
		
		Return an iterator over (*key*, *message*) pairs, where *key* is a key and
		*message* is a message representation, if called as :meth:`iteritems` or
		return a list of such pairs if called as :meth:`items`. The messages are
		represented as instances of the appropriate format-specific
		:class:`Message` subclass unless a custom message factory was specified
		when the :class:`Mailbox` instance was initialized.
		
		
		"""
		pass
		
	def get(self, key,default=None):
		"""__getitem__(key)
		
		Return a representation of the message corresponding to *key*. If no such
		message exists, *default* is returned if the method was called as
		:meth:`get` and a :exc:`KeyError` exception is raised if the method was
		called as :meth:`__getitem__`. The message is represented as an instance
		of the appropriate format-specific :class:`Message` subclass unless a
		custom message factory was specified when the :class:`Mailbox` instance
		was initialized.
		
		
		"""
		pass
		
	def get_message(self, key):
		"""
		Return a representation of the message corresponding to *key* as an
		instance of the appropriate format-specific :class:`Message` subclass, or
		raise a :exc:`KeyError` exception if no such message exists.
		
		
		"""
		pass
		
	def get_string(self, key):
		"""
		Return a string representation of the message corresponding to *key*, or
		raise a :exc:`KeyError` exception if no such message exists.
		
		
		"""
		pass
		
	def get_file(self, key):
		"""
		Return a file-like representation of the message corresponding to *key*,
		or raise a :exc:`KeyError` exception if no such message exists. The
		file-like object behaves as if open in binary mode. This file should be
		closed once it is no longer needed.
		
		"""
		pass
		
	def has_key(self, key):
		"""__contains__(key)
		
		Return ``True`` if *key* corresponds to a message, ``False`` otherwise.
		
		
		"""
		pass
		
	def __len__(self, ):
		"""
		Return a count of messages in the mailbox.
		
		
		"""
		pass
		
	def clear(self, ):
		"""
		Delete all messages from the mailbox.
		
		
		"""
		pass
		
	def pop(self, key,default):
		"""
		Return a representation of the message corresponding to *key* and delete
		the message. If no such message exists, return *default* if it was
		supplied or else raise a :exc:`KeyError` exception. The message is
		represented as an instance of the appropriate format-specific
		:class:`Message` subclass unless a custom message factory was specified
		when the :class:`Mailbox` instance was initialized.
		
		
		"""
		pass
		
	def popitem(self, ):
		"""
		Return an arbitrary (*key*, *message*) pair, where *key* is a key and
		*message* is a message representation, and delete the corresponding
		message. If the mailbox is empty, raise a :exc:`KeyError` exception. The
		message is represented as an instance of the appropriate format-specific
		:class:`Message` subclass unless a custom message factory was specified
		when the :class:`Mailbox` instance was initialized.
		
		
		"""
		pass
		
	def update(self, arg):
		"""
		Parameter *arg* should be a *key*-to-*message* mapping or an iterable of
		(*key*, *message*) pairs. Updates the mailbox so that, for each given
		*key* and *message*, the message corresponding to *key* is set to
		*message* as if by using :meth:`__setitem__`. As with :meth:`__setitem__`,
		each *key* must already correspond to a message in the mailbox or else a
		:exc:`KeyError` exception will be raised, so in general it is incorrect
		for *arg* to be a :class:`Mailbox` instance.
		
		"""
		pass
		
	def flush(self, ):
		"""
		Write any pending changes to the filesystem. For some :class:`Mailbox`
		subclasses, changes are always written immediately and :meth:`flush` does
		nothing, but you should still make a habit of calling this method.
		
		
		"""
		pass
		
	def lock(self, ):
		"""
		Acquire an exclusive advisory lock on the mailbox so that other processes
		know not to modify it. An :exc:`ExternalClashError` is raised if the lock
		is not available. The particular locking mechanisms used depend upon the
		mailbox format.  You should *always* lock the mailbox before making any
		modifications to its contents.
		
		
		"""
		pass
		
	def unlock(self, ):
		"""
		Release the lock on the mailbox, if any.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		Flush the mailbox, unlock it if necessary, and close any open files. For
		some :class:`Mailbox` subclasses, this method does nothing.
		
		
		.. class:`Maildir`
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def list_folders(self, ):
		"""
		Return a list of the names of all folders.
		
		
		"""
		pass
		
	def get_folder(self, folder):
		"""
		Return a :class:`Maildir` instance representing the folder whose name is
		*folder*. A :exc:`NoSuchMailboxError` exception is raised if the folder
		does not exist.
		
		
		"""
		pass
		
	def add_folder(self, folder):
		"""
		Create a folder whose name is *folder* and return a :class:`Maildir`
		instance representing it.
		
		
		"""
		pass
		
	def remove_folder(self, folder):
		"""
		Delete the folder whose name is *folder*. If the folder contains any
		messages, a :exc:`NotEmptyError` exception will be raised and the folder
		will not be deleted.
		
		
		"""
		pass
		
	def clean(self, ):
		"""
		Delete temporary files from the mailbox that have not been accessed in the
		last 36 hours. The Maildir specification says that mail-reading programs
		should do this occasionally.
		
		Some :class:`Mailbox` methods implemented by :class:`Maildir` deserve special
		remarks:
		
		
		"""
		pass
		
	def add(self, message):
		"""__setitem__(key, message)
		update(arg)
		
		"""
		pass
		
	def flush(self, ):
		"""
		All changes to Maildir mailboxes are immediately applied, so this method
		does nothing.
		
		
		"""
		pass
		
	def lock(self, ):
		"""unlock()
		
		Maildir mailboxes do not support (or require) locking, so these methods do
		nothing.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		:class:`Maildir` instances do not keep any open files and the underlying
		mailboxes do not support locking, so this method does nothing.
		
		
		"""
		pass
		
	def get_file(self, key):
		"""
		Depending upon the host platform, it may not be possible to modify or
		remove the underlying message while the returned file remains open.
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get_file(self, key):
		"""
		Using the file after calling :meth:`flush` or :meth:`close` on the
		:class:`mbox` instance may yield unpredictable results or raise an
		exception.
		
		
		"""
		pass
		
	def lock(self, ):
		"""unlock()
		
		Three locking mechanisms are used---dot locking and, if available, the
		:cfunc:`flock` and :cfunc:`lockf` system calls.
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def list_folders(self, ):
		"""
		Return a list of the names of all folders.
		
		
		"""
		pass
		
	def get_folder(self, folder):
		"""
		Return an :class:`MH` instance representing the folder whose name is
		*folder*. A :exc:`NoSuchMailboxError` exception is raised if the folder
		does not exist.
		
		
		"""
		pass
		
	def add_folder(self, folder):
		"""
		Create a folder whose name is *folder* and return an :class:`MH` instance
		representing it.
		
		
		"""
		pass
		
	def remove_folder(self, folder):
		"""
		Delete the folder whose name is *folder*. If the folder contains any
		messages, a :exc:`NotEmptyError` exception will be raised and the folder
		will not be deleted.
		
		
		"""
		pass
		
	def get_sequences(self, ):
		"""
		Return a dictionary of sequence names mapped to key lists. If there are no
		sequences, the empty dictionary is returned.
		
		
		"""
		pass
		
	def set_sequences(self, sequences):
		"""
		Re-define the sequences that exist in the mailbox based upon *sequences*,
		a dictionary of names mapped to key lists, like returned by
		:meth:`get_sequences`.
		
		
		"""
		pass
		
	def pack(self, ):
		"""
		Rename messages in the mailbox as necessary to eliminate gaps in
		numbering.  Entries in the sequences list are updated correspondingly.
		
		"""
		pass
		
	def remove(self, key):
		"""__delitem__(key)
		discard(key)
		
		These methods immediately delete the message. The MH convention of marking
		a message for deletion by prepending a comma to its name is not used.
		
		
		"""
		pass
		
	def lock(self, ):
		"""unlock()
		
		Three locking mechanisms are used---dot locking and, if available, the
		:cfunc:`flock` and :cfunc:`lockf` system calls. For MH mailboxes, locking
		the mailbox means locking the :file:`.mh_sequences` file and, only for the
		duration of any operations that affect them, locking individual message
		files.
		
		
		"""
		pass
		
	def get_file(self, key):
		"""
		Depending upon the host platform, it may not be possible to remove the
		underlying message while the returned file remains open.
		
		
		"""
		pass
		
	def flush(self, ):
		"""
		All changes to MH mailboxes are immediately applied, so this method does
		nothing.
		
		
		"""
		pass
		
	def close(self, ):
		"""
		:class:`MH` instances do not keep any open files, so this method is
		equivalent to :meth:`unlock`.
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get_labels(self, ):
		"""
		Return a list of the names of all user-defined labels used in the mailbox.
		
		"""
		pass
		
	def get_file(self, key):
		"""
		In Babyl mailboxes, the headers of a message are not stored contiguously
		with the body of the message. To generate a file-like representation, the
		headers and body are copied together into a :class:`StringIO` instance
		(from the :mod:`StringIO` module), which has an API identical to that of a
		file. As a result, the file-like object is truly independent of the
		underlying mailbox but does not save memory compared to a string
		representation.
		
		
		"""
		pass
		
	def lock(self, ):
		"""unlock()
		
		Three locking mechanisms are used---dot locking and, if available, the
		:cfunc:`flock` and :cfunc:`lockf` system calls.
		
		
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get_file(self, key):
		"""
		Using the file after calling :meth:`flush` or :meth:`close` on the
		:class:`MMDF` instance may yield unpredictable results or raise an
		exception.
		
		
		"""
		pass
		
	def lock(self, ):
		"""unlock()
		
		Three locking mechanisms are used---dot locking and, if available, the
		:cfunc:`flock` and :cfunc:`lockf` system calls.
		
		
		"""
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
	
	
	def __init__(self, ):
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
	
	
	def __init__(self, ):
		pass
	
	def get_subdir(self, ):
		"""
		Return either "new" (if the message should be stored in the :file:`new`
		subdirectory) or "cur" (if the message should be stored in the :file:`cur`
		subdirectory).
		
		"""
		pass
		
	def set_subdir(self, subdir):
		"""
		Set the subdirectory the message should be stored in. Parameter *subdir*
		must be either "new" or "cur".
		
		
		"""
		pass
		
	def get_flags(self, ):
		"""
		Return a string specifying the flags that are currently set. If the
		message complies with the standard Maildir format, the result is the
		concatenation in alphabetical order of zero or one occurrence of each of
		``'D'``, ``'F'``, ``'P'``, ``'R'``, ``'S'``, and ``'T'``. The empty string
		is returned if no flags are set or if "info" contains experimental
		semantics.
		
		
		"""
		pass
		
	def set_flags(self, flags):
		"""
		Set the flags specified by *flags* and unset all others.
		
		
		"""
		pass
		
	def add_flag(self, flag):
		"""
		Set the flag(s) specified by *flag* without changing other flags. To add
		more than one flag at a time, *flag* may be a string of more than one
		character. The current "info" is overwritten whether or not it contains
		experimental information rather than flags.
		
		
		"""
		pass
		
	def remove_flag(self, flag):
		"""
		Unset the flag(s) specified by *flag* without changing other flags. To
		remove more than one flag at a time, *flag* maybe a string of more than
		one character.  If "info" contains experimental information rather than
		flags, the current "info" is not modified.
		
		
		"""
		pass
		
	def get_date(self, ):
		"""
		Return the delivery date of the message as a floating-point number
		representing seconds since the epoch.
		
		
		"""
		pass
		
	def set_date(self, date):
		"""
		Set the delivery date of the message to *date*, a floating-point number
		representing seconds since the epoch.
		
		
		"""
		pass
		
	def get_info(self, ):
		"""
		Return a string containing the "info" for a message. This is useful for
		accessing and modifying "info" that is experimental (i.e., not a list of
		flags).
		
		
		"""
		pass
		
	def set_info(self, info):
		"""
		Set "info" to *info*, which should be a string.
		
		When a :class:`MaildirMessage` instance is created based upon an
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get__from(self, ):
		"""
		Return a string representing the "From " line that marks the start of the
		message in an mbox mailbox. The leading "From " and the trailing newline
		are excluded.
		
		
		"""
		pass
		
	def set__from(self, _from_,time_=None):
		"""
		Set the "From " line to *from_*, which should be specified without a
		leading "From " or trailing newline. For convenience, *time_* may be
		specified and will be formatted appropriately and appended to *from_*. If
		*time_* is specified, it should be a :class:`struct_time` instance, a
		tuple suitable for passing to :meth:`time.strftime`, or ``True`` (to use
		:meth:`time.gmtime`).
		
		
		"""
		pass
		
	def get_flags(self, ):
		"""
		Return a string specifying the flags that are currently set. If the
		message complies with the conventional format, the result is the
		concatenation in the following order of zero or one occurrence of each of
		``'R'``, ``'O'``, ``'D'``, ``'F'``, and ``'A'``.
		
		
		"""
		pass
		
	def set_flags(self, flags):
		"""
		Set the flags specified by *flags* and unset all others. Parameter *flags*
		should be the concatenation in any order of zero or more occurrences of
		each of ``'R'``, ``'O'``, ``'D'``, ``'F'``, and ``'A'``.
		
		
		"""
		pass
		
	def add_flag(self, flag):
		"""
		Set the flag(s) specified by *flag* without changing other flags. To add
		more than one flag at a time, *flag* may be a string of more than one
		character.
		
		
		"""
		pass
		
	def remove_flag(self, flag):
		"""
		Unset the flag(s) specified by *flag* without changing other flags. To
		remove more than one flag at a time, *flag* maybe a string of more than
		one character.
		
		When an :class:`mboxMessage` instance is created based upon a
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get_sequences(self, ):
		"""
		Return a list of the names of sequences that include this message.
		
		
		"""
		pass
		
	def set_sequences(self, sequences):
		"""
		Set the list of sequences that include this message.
		
		
		"""
		pass
		
	def add_sequence(self, sequence):
		"""
		Add *sequence* to the list of sequences that include this message.
		
		
		"""
		pass
		
	def remove_sequence(self, sequence):
		"""
		Remove *sequence* from the list of sequences that include this message.
		
		When an :class:`MHMessage` instance is created based upon a
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get_labels(self, ):
		"""
		Return a list of labels on the message.
		
		
		"""
		pass
		
	def set_labels(self, labels):
		"""
		Set the list of labels on the message to *labels*.
		
		
		"""
		pass
		
	def add_label(self, label):
		"""
		Add *label* to the list of labels on the message.
		
		
		"""
		pass
		
	def remove_label(self, label):
		"""
		Remove *label* from the list of labels on the message.
		
		
		"""
		pass
		
	def get_visible(self, ):
		"""
		Return an :class:`Message` instance whose headers are the message's
		visible headers and whose body is empty.
		
		
		"""
		pass
		
	def set_visible(self, visible):
		"""
		Set the message's visible headers to be the same as the headers in
		*message*.  Parameter *visible* should be a :class:`Message` instance, an
		:class:`email.Message.Message` instance, a string, or a file-like object
		(which should be open in text mode).
		
		
		"""
		pass
		
	def update_visible(self, ):
		"""
		When a :class:`BabylMessage` instance's original headers are modified, the
		visible headers are not automatically modified to correspond. This method
		updates the visible headers as follows: each visible header with a
		corresponding original header is set to the value of the original header,
		each visible header without a corresponding original header is removed,
		and any of :mailheader:`Date`, :mailheader:`From`, :mailheader:`Reply-To`,
		:mailheader:`To`, :mailheader:`CC`, and :mailheader:`Subject` that are
		present in the original headers but not the visible headers are added to
		the visible headers.
		
		When a :class:`BabylMessage` instance is created based upon a
		"""
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
	
	
	def __init__(self, ):
		pass
	
	def get__from(self, ):
		"""
		Return a string representing the "From " line that marks the start of the
		message in an mbox mailbox. The leading "From " and the trailing newline
		are excluded.
		
		
		"""
		pass
		
	def set__from(self, _from_,time_=None):
		"""
		Set the "From " line to *from_*, which should be specified without a
		leading "From " or trailing newline. For convenience, *time_* may be
		specified and will be formatted appropriately and appended to *from_*. If
		*time_* is specified, it should be a :class:`struct_time` instance, a
		tuple suitable for passing to :meth:`time.strftime`, or ``True`` (to use
		:meth:`time.gmtime`).
		
		
		"""
		pass
		
	def get_flags(self, ):
		"""
		Return a string specifying the flags that are currently set. If the
		message complies with the conventional format, the result is the
		concatenation in the following order of zero or one occurrence of each of
		``'R'``, ``'O'``, ``'D'``, ``'F'``, and ``'A'``.
		
		
		"""
		pass
		
	def set_flags(self, flags):
		"""
		Set the flags specified by *flags* and unset all others. Parameter *flags*
		should be the concatenation in any order of zero or more occurrences of
		each of ``'R'``, ``'O'``, ``'D'``, ``'F'``, and ``'A'``.
		
		
		"""
		pass
		
	def add_flag(self, flag):
		"""
		Set the flag(s) specified by *flag* without changing other flags. To add
		more than one flag at a time, *flag* may be a string of more than one
		character.
		
		
		"""
		pass
		
	def remove_flag(self, flag):
		"""
		Unset the flag(s) specified by *flag* without changing other flags. To
		remove more than one flag at a time, *flag* maybe a string of more than
		one character.
		
		When an :class:`MMDFMessage` instance is created based upon a
		"""
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
	
	
	def __init__(self, ):
		pass
	
	


class PortableUnixMailbox:


	"""
	A less-strict version of :class:`UnixMailbox`, which considers only the ``From``
	at the beginning of the line separating messages.  The "*name* *time*" portion
	of the From line is ignored, to protect against some variations that are
	observed in practice.  This works since lines in the message which begin with
	``'From '`` are quoted by mail handling software at delivery-time.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class MmdfMailbox:


	"""
	Access an MMDF-style mailbox, where all messages are contained in a single file
	and separated by lines consisting of 4 control-A characters.  The file object
	*fp* points to the mailbox file. Optional *factory* is as with the
	:class:`UnixMailbox` class.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


class MHMailbox:


	"""
	Access an MH mailbox, a directory with each message in a separate file with a
	numeric name. The name of the mailbox directory is passed in *dirname*.
	*factory* is as with the :class:`UnixMailbox` class.
	
	
	"""
	
	
	def __init__(self, ):
		pass
	
	


