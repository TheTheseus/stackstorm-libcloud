from lib.actions import BaseAction

__all__ = [
    'DestroyContainerAction'
]


class DestroyContainerAction(BaseAction):
    api_type = 'container'

    def run(self, credentials, container_id, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        container = driver.get_container(container_id)

        self.logger.info('Destroying container: %s...' % (container))
        status = driver.destroy_container(container, **extra_kwargs)

        if status is True:
            self.logger.info('Successfully destroyed container "%s"' % (container))
        else:
            self.logger.error('Failed to destroy container "%s"' % (container))

        return status
