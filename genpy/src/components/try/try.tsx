import classNames from 'classnames';
import styles from './try.module.scss';

export interface TryProps {
    className?: string;
}

/**
 * This component was created using Codux's Default new component template.
 * To create custom component templates, see https://help.codux.com/kb/en/article/kb16522
 */
export const Try = ({ className }: TryProps) => {
    return <div className={classNames(styles.root, className)}>Try</div>;
};
