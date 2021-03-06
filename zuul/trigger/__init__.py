# Copyright 2014 Rackspace Australia
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class BaseTrigger(object):
    """Base class for triggers.

    Defines the exact public methods that must be supplied."""

    def __init__(self, trigger_config={}, sched=None, connection=None):
        self.trigger_config = trigger_config
        self.sched = sched
        self.connection = connection

    def __repr__(self):
        return "<%s connection: %s>" % (
            self.__class__.__name__,
            self.connection
        )

    def stop(self):
        """Stop the trigger."""

    @abc.abstractmethod
    def getEventFilters(self, trigger_conf):
        """Return a list of EventFilter's for the scheduler to match against.
        """

    def postConfig(self):
        """Called after config is loaded."""

    def onChangeMerged(self, change, source):
        """Called when a change has been merged."""

    def onChangeEnqueued(self, change, pipeline):
        """Called when a change has been enqueued."""
